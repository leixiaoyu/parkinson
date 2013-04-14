#data sampler
import os
import random
from time import strftime


def File_Len(file_path):
    # return number of rows in a file
    # full path, including file name, is needed
    with open(file_path) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def Read_File(file_path):
    # return lists containing data within the given file
    # full path, including file name, is needed
    fname = file_path
    with open(fname, 'r') as f:
        f.next()
        matrix, row = [], []
        for line in f:
            temp = line.split(',')
            for e in temp[:-1]:
                try:
                    row.append(float(e))
                except:
                    print 'not able to convert: ' + e
                    row.append(-999)
            matrix.append(row)
            row = []
    return matrix


def Normalize_DateTime(dt):
    # convert date time into integers
    chs = ['-', ' ', ':']
    for ch in chs:
        dt = dt.replace(ch, '')
    return int(dt)


def Get_Timestamp():
    ctime = strftime("%Y-%m-%d-%H-%M-%S")
    return str(ctime).replace('-', '')


def Lotter_w_Rep(sample_size):
    dout = []
    i = sample_size
    while i > 0:
        dout.append(random.randint(0, i))
        i -= 1
    return dout.sort()


def Sampling_w_Rep(src_file, tgt_dir, size):
    """sampling data in source file without replacement and save into target file"""
    length = File_Len(src_file)
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
    """sampling data in source file without replacement and save into target file"""
    length = File_Len(src_file)
    if size > length:
        size = length - 1
    tags, used = [], []
    i = size
    while i > 0:
        tag = random.randint(0, i)
        while tag in used:
            tag = random.randint(0, i)
        tags.append(tag)
        i -= 1
    fout_path = tgt_dir + os.path.basename(src_file)[:-4] + '_sample.csv'
    fout = open(fout_path, 'w')
    with open(src_file, 'r') as fin:
        for i, line in enumerate(fin):
            if i in tags:
                fout.write(line)
    fout.close()
    tags, used = [], []


def Summerize_Time(candidate, keywords, src_dir, tgt_dir):
    times = []
    for kw in keywords:
        fin_fullname = src_dir + candidate + '_' + kw + '_mean.csv'
        times_i = []
        with open(fin_fullname, 'r') as fin:
            for line in fin:
                time = Normalize_DateTime(line[-1])
                times_i.append(time)
            times.append(times_i)


def Take_Rows(src_file, tgt_dir, number_of_row):
    n = number_of_row
    ctime = Get_Timestamp().replace('-', '')
    fout = open(tgt_dir + os.path.splitext(src_file)[0] + '_sample' + ctime + '.csv', 'a+')
    with open(src_file, 'r') as fin:
        counter = 0
        for line in fin:
            if counter > n:
                break
            else:
                fout.write(line)
    fout.close
