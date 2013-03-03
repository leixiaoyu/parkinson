# data aggregator
import ConfigParser
import os
import numpy
import gen_utils as gu

#<<<<<<< HEAD
import ConfigParser

print 'DONE'

config = ConfigParser.RawConfigParser()
config.read('localconfig.conf')
calculated_dir = config.get('Pathes', 'calculated')
merged_dir = config.get('Pathes', 'merged')
candidates = config.get('Types', 'candidate').split(',')
keywords = config.get('Types', 'keyword').split(',')

def Stat_Calculator(candidate, keyword, src_dir, tgt_dir):
    minute_table = []
    minute_table2 = []
    minute_table3 = []
    mean_result2 = []
    src_file = src_dir + candidate + '_' + keyword + '.csv'
    benchmark = ''
    fout_name = candidate + '_' + keyword + '_mean' + '.csv'
    fout_fullpath = tgt_dir + fout_name    
    fout = open(fout_fullpath, 'a+')
    flag = 1
    with open(src_file) as f:   #write the title                    
        for i in f:
            if flag ==1:
                fout.write(i)
                flag =2    
    with open(src_file) as f:   #write the mean for each minute             
        f.next()
        counter = 1
        for line in f:
            if counter == 1:
                benchmark = line.split(',')[-1]
                minute_table.append(line.split(','))
            else:
                ctime = line.split(',')[-1]
                if gu.Is_Same_Minute(benchmark, ctime):  #identify each minute
                    for i in line.split(',')[:-1]:
                        i = float(i)
                    minute_table.append(line.split(','))
                else:
                    # calculation 
                                        
                    for i in minute_table:
                        for j in i[0:-1]:
                            j = float(j)
                        minute_table2.append(i[0:-1])
                    minute_table3=minute_table2
                    for i in range(len(minute_table2)):
                        for j in range(len(minute_table2[0])):                                
                                minute_table3[i][j] = float(minute_table2[i][j])                   
                    mean_result = numpy.mean(minute_table3, axis=0)                    
#                    variance_result = numpy.var(minute_table3, axis=0)
                    for i in mean_result:
                        mean_result2.append(i)
                    mean_result2.append(benchmark)
                    # end of calculation
                    fout.write(str(mean_result2)+ '\n') #write into file
                    # reset elements
                    benchmark = line.split(',')[-1]
                    minute_table = []
                    minute_table2 = []
                    minute_table3 = []
                    mean_result2 = []
                    minute_table.append(line.split(','))
            counter += 1
        f.next
<<<<<<< HEAD
=======
    
        
for c in candidates:
	for kw in keywords:
		Stat_Calculator(c, kw, merged_dir, calculated_dir)
>>>>>>> 31031744a8eea049d013e5a0908f84e387e9ded5

print 'done'
#>>>>>>> calculator


