# general utilities
import numpy as np

def Compare_DateTime(dt1, dt2):
	# return true if dt2 is later than dt1
	chs = [ '-', ' ', ':' ]
	for ch in chs:
		dt1 = dt1.replace(ch, '')
		dt2 = dt2.replace(ch, '')
	dtint1 = int(dt1)
	dtint2 = int(dt2)
	if dtint1 < dtint2:
		return True
	else:
		return False

def Is_Same_Minute(dt1, dt2):
	# return true if dt2 is in the same minute as dt1
	chs = [ '-', ' ', ':' ]
	for ch in chs:
		dt1 = dt1.replace(ch, '')
		dt2 = dt2.replace(ch, '')
	if dt1[:12] == dt2[:12]:
		return True
	else:
		return False

def Compute_Mean(data_list):
	data = np.array(data_list)
	dout = []
	mean = np.mean(data, axis=0)
	for c in mean:
		dout.append(c)
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

