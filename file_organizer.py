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
			tar.extractall(target_folder + '/' + os.path.basename(f))

def CleanDir(directory):
	walker = os.walk(directory)
	for data in walker:
		for files in data[2]:
			try:
				shutil.move(data[0] + '/' + files, directory)
			except shutil.Error:
				continue

def Mergy(keyword,tarf):
	files_full = os.listdir(tarf)
	if not os.path.isdir(tarf):
		os.makedirs(tarf)
	os.chdir(csd)
	fout=open(keyword +'.csv','a+')	
	t=1   #flag	
	for f in files_full:
		if len(f) > 9:			
			if str(keyword) == f.split('_')[1]:
				if t==1:     # first file:
					lines=open(f,'r')
					t=2
					for line in lines:
						fout.write(line)
				else:       # others						
					lines=open(f,'r')
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
# Mergy('accel',csd)

# calculate average value




print 'DONE'
		
