# data aggregator
import ConfigParser
import gen_utils as gu

config = ConfigParser.RawConfigParser()
config.read('localconfig.conf')
calculated_dir = config.get('Pathes', 'calculated')
merged_dir = config.get('Pathes', 'merged')
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
                flag = 2
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
                elif gu.Is_Same_Minute(benchmark, ctime):  # identify each minute
                    for i in line.split(',')[:-1]:
                        i = float(i)
                        temp_line.append(i)
                    minute_table.append(temp_line)
                else:
                    print 'Wrong Branch'

for c in candidates:
	for kw in keywords:
		Stat_Calculator(c, kw, merged_dir, calculated_dir)

print 'DONE'
