#data sampler
import gen_utils as gu
import os
import random


def Lotter_w_Rep(sample_size):
    dout = []
    i = sample_size
    while i > 0:
        dout.append(random.randint(0, i))
        i -= 1
    return dout.sort()


def Lotter_wo_Rep(sample_size):
    dout, used = [], []
    i = sample_size
    while i > 0:
        tag = random.randint(0, i)
        while tag in used:
            tag = random.randint(0, 1)
        dout.append(tag)
        i -= 1
    return dout.sort()


def Sampling_w_Rep(src_file, tgt_dir, size):
    length = gu.File_Len(src_file)
    if size > length:
        size = length - 1
    tags = Lotter_w_Rep(size)
    fout_path = tgt_dir + os.path.splitext(src_file)[0] + '_sample.csv'
    fout = open(fout_path, 'w')
    with open(src_file, 'r') as fin:
        for i, line in enumerate(fin):
            if i in tags:
                fout.write(line)
    fout.close()


def Sampling_without_Rep(src_file, tgt_dir, size):
    length = gu.File_Len(src_file)
    if size > length:
        size = length - 1
    tags = Lotter_wo_Rep(size)
    fout_path = tgt_dir + os.path.splitext(src_file)[0] + '_sample.csv'
    fout = open(fout_path, 'w')
    with open(src_file, 'r') as fin:
        for i, line in enumerate(fin):
            if i in tags:
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


def Take_Rows(src_file, tgt_dir, number_of_row):
    n = number_of_row
    ctime = gu.Get_Timestamp().replace('-', '')
    fout = open(tgt_dir + os.path.splitext(src_file)[0] + '_sample' + ctime + '.csv', 'a+')
    with open(src_file, 'r') as fin:
        counter = 0
        for line in fin:
            if counter > n:
                break
            else:
                fout.write(line)
    fout.close
