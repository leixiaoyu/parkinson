# data summizer
import ConfigParser
import os

config = ConfigParser.RawConfigParser()
config.read('localconfig.conf')
log_dir = config.get('Pathes', 'log')
merged_dir = config.get('Pathes', 'merged')
calculated_dir = config.get('Pathes', 'calculate')


def File_Len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def File_Summary(path, logfile):
    files = os.listdir(path)
    logfile.write('counter | file name | size | attributes | instances\n')
    counter = 1
    for f in files:
        size = os.path.getsize(path + f)
        inst_num = File_Len(path + f)
        att_num = 0
        with open(path + f) as temp:
            att_num = len(temp.readline().split(','))
        message = str(counter) + ' | ' + f + ' | ' + str(size) + ' | ' + str(att_num) + ' | ' + str(inst_num) + '\n'
        logfile.write(message)
        counter += 1

# summarized data files in given path
# make sure to change theme to match log file contents

# ctime = strftime("%Y-%m-%d_%H-%M-%S")
# theme = 'summary'
# log_name = ctime + '_' + theme + '.log'

# with open(log_dir + log_name, 'wb') as logfile:
#     File_Summary(calculated_dir, logfile)

# print 'DONE'
