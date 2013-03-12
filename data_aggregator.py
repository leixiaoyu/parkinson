# data aggregator
import ConfigParser
import gen_utils as gu
import math

config = ConfigParser.RawConfigParser()
config.read('localconfig.conf')
calculated_dir = config.get('Pathes', 'calculate')
merged_dir = config.get('Pathes', 'merged')
log_dir = config.get('Pathes', 'log')
test_dir = config.get('Pathes', 'test')
candidates = config.get('Types', 'candidate').split(',')
keywords = config.get('Types', 'keyword').split(',')


def Stat_Calculator(candidate, keyword, src_dir, tgt_dir):
    minute_table = []
    src_file = src_dir + candidate + '_' + keyword + '.csv'
    benchmark = ''
    fout_name = candidate + '_' + keyword + '_mean' + '.csv'
    fout_fullpath = tgt_dir + fout_name
    fout = open(fout_fullpath, 'a+')
    flag = 1
    with open(src_file) as f:
        for line in f:
            if flag == 1:
                fout.write(line)  # write title in output file
            else:  # calculate mean and write to output file
                temp_line = []
                ctime = line.split(',')[-1]
                if benchmark == '':
                    benchmark = line.split(',')[-1]
                    for i in line.split(',')[:-1]:
                        i = float(i)
                        temp_line.append(i)
                    minute_table.append(temp_line)
                elif not gu.Is_Same_Minute(benchmark, ctime):
                    mean_result = gu.Compute_Mean(minute_table)
                    for c in mean_result:
                        c = str(c)
                    mean_result.append(benchmark)
                    gu.Write_String_List(mean_result, fout, ',')
                    benchmark = line.split(',')[-1]
                    minute_table = []
                    for i in line.split(',')[:-1]:
                        i = float(i)
                        temp_line.append(i)
                    minute_table.append(temp_line)
                elif gu.Is_Same_Minute(benchmark, ctime):  # identify each minute
                    for i in line.split(',')[:-1]:
                        i = float(i)
                        temp_line.append(i)
                    minute_table.append(temp_line)
                else:
                    print 'Wrong Branch'
            print flag
            flag += 1


def T_Test(can1, can2, keyword, column, src_dir, tgt_dir):
    can1_path = src_dir + can1 + '_' + keyword + '.csv'
    can2_path = src_dir + can2 + '_' + keyword + '.csv'
    fin1 = open(can1_path, 'r')
    fin2 = open(can2_path, 'r')
    timestamp = gu.Get_Timestamp().replace('-', '')[4:]
    fout_path = tgt_dir + can1 + '_' + can2 + '_ttest_' + timestamp + '.log'
    data1, data2 = [], []
    counter = 0
    for line in fin1:
        if counter < 2:
            counter += 1
        else:
            data1.append(line[column])
    for line in fin2:
        if counter < 2:
            counter += 1
        else:
            data2.append(line[column])
    fout = open(fout_path, 'a+')
    mean1, var1 = gu.Compute_Mean_Variance(data1)
    mean2, var2 = gu.Compute_Mean_Variance(data2)
    n1, n2 = len(data1), len(data2)
    fout.write(str(mean1) + '\n' + str(var1) + '\n')
    fout.write(str(mean2) + '\n' + str(var2) + '\n')
    t = (mean1 - mean2) / math.sqrt(var1 / n1 + var2 / n2)
    fout.write(str(t) + '\n')


def ANOVA(candidates, keyword, column, src_dir, tgt_dir):
    data_i, data_matrix_raw, data_matrix, file_lens = [], [], [], []
    # read data into lists
    for c in candidates:
        with open(src_dir + c + '_' + keyword + '.csv', 'r') as fin:
            file_lens.append(gu.File_Len(fin))
            counter = 0
            for line in fin:
                if counter == 0:
                    counter = 1
                else:
                    data_i.append(line[column])
        data_matrix_raw.append(data_i)
        data_i = []
    sample_size = min(file_lens) - 1
    # sample data so every candidate has the same number of instances
    for d in data_matrix_raw:
        # sampling without replacement
        sample = gu.Sampling_with_Rep(d, sample_size)
        data_matrix.append(sample)
    # start calculate states for ANOVA
    means = gu.Compute_Mean(data_matrix)



# T_Test('LILLY', 'PEONY', 'accel', 3, test_dir, log_dir)

# for c in candidates:
#     print c
#     for kw in keywords:
#         print kw
#         Stat_Calculator(c, kw, merged_dir, calculated_dir)

print 'DONE'
