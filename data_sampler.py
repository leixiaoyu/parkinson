# data sampler

import ConfigParser
import gen_utils as gu
import random

config = ConfigParser.RawConfigParser()
config.read('localconfig.conf')
sample_dir = config.get('Pathes', 'sample')
merged_dir = config.get('Pathes', 'merged')
calculated_dir = config.get('Pathes', 'calculate')
candidates = config.get('Types', 'candidate').split(',')
keywords = config.get('Types', 'keyword').split(',')


def File_Len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def Sample_Calculated_Data(candidate, keyword, src_dir, tgt_dir, size):
    src_file = src_dir + candidate + '_' + keyword + '_mean.csv'
    length = File_Len(src_file)
    used_num = [0]
    if size > length:
        size = length - 1
    for i in range(size):
        ran = random.randint(1, length)
        while ran in used_num:
            ran = random.randint(1, length)
        used_num.append(ran)
    used_num.sort()
    fout_path = tgt_dir + candidate + '_' + keyword + '_sample_calculated.csv'
    fout = open(fout_path, 'w')
    with open(src_file, 'r') as fin:
        for i, line in enumerate(fin):
            if i in used_num:
                fout.write(line)
    fout.close()


def Sample_Raw_Data(candidate, keyword, src_dir, tgt_dir, size):
    src_file = src_dir + candidate + '_' + keyword + '.csv'
    length = File_Len(src_file)
    used_num = [0]
    if size > length:
        size = length - 1
    for i in range(size):
        ran = random.randint(1, length)
        while ran in used_num:
            ran = random.randint(1, length)
        used_num.append(ran)
    used_num.sort()
    fout_path = tgt_dir + candidate + '_' + keyword + '_sample_raw.csv'
    fout = open(fout_path, 'w')
    with open(src_file, 'r') as fin:
        for i, line in enumerate(fin):
            if i in used_num:
                fout.write(line)
    fout.close()


def Summerize_Time(candidate, keywords, src_dir, tgt_dir):
    times = []
    for kw in keywords:
        fin_fullname = src_dir + candidate + '_' + kw + '_mean.csv'
        times_i = []
        with open(fin_fullname, 'r') as fin:
            for line in fin:
                time = gu.Normalize_DateTime(line[-1])
                times_i.append(time)
            times.append(times_i)


# print candidates
# print keywords

candidate = 'DAISEY'
keyword = 'accel'
Sample_Calculated_Data(candidate, keyword, calculated_dir, sample_dir, 100)

# for c in candidates:
#     for kw in keywords:
#         Sampler(c, kw, merged_dir, sample_dir, 100)

print 'DONE'
