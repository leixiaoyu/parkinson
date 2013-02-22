# data file organizer
# written in python

import shutil
import os
import tarfile

# define working path and resources

cwd = os.getcwd()
csd = '/Users/xiaoyu/Documents/parkinson_data/MJFF-Data/'
ctd = '/Users/xiaoyu/Documents/parkinson_data/processing/'
print 'Current working directory: ' + cwd
print 'Current source directory: ' + csd
print 'Current target directory: ' + ctd

# define working methods

def ExtractFiles(source_folder):
	files_full = os.listdir(source_folder)
	for f in files_full:
		if len(f) > 9:
			candidate_name = f.split('_')[1]
			target_folder = ctd + candidate_name
			if not os.path.isdir(target_folder):
				os.makedirs(target_folder)
			tarfile = tarfile.open(csd + f)
			tarfile.extractall(target_folder + '/' + os.path.basename(f))

def CleanDir(directory):
	walker = os.walk(directory)
	for data in walker:
		for files in data[2]:
			try:
				shutil.move(data[0] + '/' + files, directory)
			except shutil.Error:
				continue

# execution

candidate_list = os.listdir(ctd)
for c in candidate_list:
	CleanDir(ctd + c)
print 'DONE'
		
