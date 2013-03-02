# data aggregator
import ConfigParser
import os
import numpy
import gen_utils as gu

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('localconfig.conf')
calculated_dir = config.get('Pathes', 'calculated')
merged_dir = config.get('Pathes', 'merged')
candidates = config.get('Types', 'candidate').split(',')
keywords = config.get('Types', 'keyword').split(',')

def Stat_Calculator(candidate, keyword, src_dir, tgt_dir):
    minute_table = []
    element = []
    src_file = src_dir + candidate + '_' + keyword + '.csv'
    benchmark = ''
    fout_name = candidate + '_' + keyword + mean + '.csv'
    fout_fullpath = tgt_dir + fout_name    
    fout = open(fout_fullpath, 'a+')
    with open(src_file) as f:
        counter = 1
        for line in f:
            if counter == 1:
                benchmark = line.split(',')[-1]
                minute_table.append(line.split(','))
            else:
                ctime = line.split(',')[-1]
                if gu.Is_Same_Minute(benchmark, ctime):
                    for i in line.split(',')[:-1]:
                        i = float(i)
                    minute_table.append(line.split(','))
                else:
                    # calculation 
                    mean_result = mean(minute_table, axis=0)
                    fout.write(mean_result)
                    benchmark = line.split(',')[-1]
                    minute_table = []
                    minute_table.append(line.split(','))
            counter += 1
        f.next
    
        
print 'done'


