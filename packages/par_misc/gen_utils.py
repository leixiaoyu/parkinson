# general utilities
import numpy as np
import random
from time import strftime


def File_Len(file_path):
    with open(file_path) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def Normalize_DateTime(dt):
    chs = ['-', ' ', ':']
    for ch in chs:
        dt = dt.replace(ch, '')
    return int(dt)


def Compare_DateTime(dt1, dt2):
# return true if dt2 is later than dt1
    dtint1 = Normalize_DateTime(dt1)
    dtint2 = Normalize_DateTime(dt2)
    if dtint1 < dtint2:
        return True
    else:
        return False


def Is_Same_Minute(dt1, dt2):
    # return true if dt2 is in the same minute as dt1
    chs = ['-', ' ', ':']
    for ch in chs:
        dt1 = dt1.replace(ch, '')
        dt2 = dt2.replace(ch, '')
    if dt1[:12] == dt2[:12]:
        return True
    else:
        return False


def Get_Timestamp():
    ctime = strftime("%Y-%m-%d-%H-%M-%S")
    return str(ctime)


def Compute_Mean(data_matrix):
    data = np.array(data_matrix)
    dout = []
    mean = np.mean(data, axis=0)
    for c in mean:
        dout.append(c)
    return dout


def Compute_Mean_Variance(data_list):
    dl = data_list
    s, s2 = 0, 0
    for e in dl:
        try:
            s += float(e)
            s2 += float(e) * float(e)
        except:
            print e
    mean = s / len(dl)
    variance = (s2 - (s * s) / len(dl)) / len(dl)
    return (mean, variance)


def Sampling_with_Rep(data_list, sample_size):
    dout = []
    i = sample_size
    while i > 0:
        tag = random.randint(0, i)
        dout.append(data_list[tag])
        i -= 1
    return dout


def Sampling_without_Rep(data_list, sample_size):
    dout, used = [], []
    i = sample_size
    while i > 0:
        tag = random.randint(0, i)
        while tag in used:
            tag = random.randint(0, 1)
        dout.append(data_list[tag])
        i -= 1
    return dout


def Write_String_List(data_list, output_file, delimiter):
    data = data_list
    fout = output_file
    if len(data) > 0:
        if type(data[0]) == type(list()):
            print '1'
            for r in data:
                line = str(r[0])
                for c in r[1:]:
                    line = line + delimiter + ' ' + str(c)
                fout.write(line + '\n')
        else:
            line = str(data[0])
            for c in data[1:]:
                line = line + delimiter + ' ' + str(c)
            fout.write(line)
    else:
        print 'Empty List'
