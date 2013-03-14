# general utilities
import numpy as np


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
