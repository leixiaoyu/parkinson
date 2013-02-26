# data file organizer
# written in python

import shutil
import os
import tarfile

# define working path and resources

cwd = os.getcwd()
csd = '/Users/xiaoyu/Documents/parkinson_data/MJFF-Data/'
ctd = '/Users/xiaoyu/Documents/parkinson_data/processing/'
# csd = 'I:/csv/'
# ctd = 'H:/data challenge/APPLE/MergedFiles/'
print 'Current working directory: ' + cwd
print 'Current source directory: ' + csd
print 'Current target directory: ' + ctd

# define working methods

def ExtractFiles(src_folder, tgt_folder):
	files_full = os.listdir(src_folder)
	for f in files_full:
		if len(f) > 9:
			candidate_name = f.split('_')[1]
			target_folder = tgt_folder + candidate_name
			if not os.path.isdir(target_folder):
				os.makedirs(target_folder)
			tar = tarfile.open(src_folder + f)
			tar.extractall(target_folder)

def CleanDir(directory):
	walker = os.walk(directory)
	for data in walker:
		for files in data[2]:
			try:
				shutil.move(data[0] + '/' + files, directory)
			except shutil.Error:
				continue

def Mergy(keyword,tgt_f):
	files_full = os.listdir(tgt_f)
	os.chdir(tgt_f)
	fout=open(keyword + '.csv','a+')	
	t = 1   # flag	
	for f in files_full:
		f_path = tgt_f + f
		if os.path.splitext(f_path)[0] == keyword:
			os.remove(f_path)
		elif os.path.splitext(f_path)[1] == '.csv':
			print f_path
			if keyword == f.split('_')[1]:
				print f_path
				if t == 1:     # first file:
					lines = open(f_path,'r')
					t = 2
					for line in lines:
						fout.write(line)
				else:       # others						
					lines = open(f_path,'r')
					lines.next()
					for line in lines:
						fout.write(line)
	fout.close()
	
def AverageCalculator(data_file):
	input_data = open(data_file, 'r')
	lineTemp = []
	

# execution

#ExtractFiles(csd,ctd)
#candidate_list = os.listdir(ctd)
#for c in candidate_list:
#	CleanDir(ctd + c)




data_folders = os.listdir(ctd)
data_types = [ 'accel', 'audio', 'batt', 'cmpss', 'gps', 'meta' ]
for df in data_folders:
	if df == 'APPLE':
		tgt_folder = ctd + df + '/'
		print tgt_folder
		for dt in data_types:
			print dt
			Mergy(dt,tgt_folder)

# calculate average value

print 'DONE'
		
