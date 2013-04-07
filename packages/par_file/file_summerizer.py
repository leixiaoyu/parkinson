# data summizer
import os
from time import strftime


def File_Len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def Get_Timestamp():
    ctime = strftime("%Y-%m-%d-%H-%M-%S")
    return str(ctime).replace('-', '')


def File_Summary(src_dir, log_dir, log_name):
    """summize file property into a log file"""
    files = os.listdir(src_dir)
    log_name = log_dir + log_name + Get_Timestamp() + '.log'
    with open(log_name, 'w') as logfile:
        logfile.write('counter | file name | size | attributes | instances\n')
        counter = 1
        for f in files:
            size = os.path.getsize(src_dir + f)
            inst_num = File_Len(src_dir + f)
            att_num = 0
            with open(src_dir + f) as temp:
                att_num = len(temp.readline().split(','))
            message = str(counter) + ' | ' + f + ' | ' + str(size) + ' | ' + str(att_num) + ' | ' + str(inst_num) + '\n'
            logfile.write(message)
            counter += 1
