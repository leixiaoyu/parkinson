# data file organizer
# written in python

import os
import tarfile

cwd = os.getcwd()
csd = '/Users/xiaoyu/Documents/parkinson_data/MJFF-Data/'
ctd = '/Users/xiaoyu/Documents/parkinson_data/processing/'
print 'Current working directory: ' + cwd
print 'Current source directory: ' + csd
print 'Current target directory: ' + ctd
files_full = os.listdir(folder_path)
for f in files_full:
	if len(f) > 9:
		candidate_name = f.split('_')[1]
		target_folder = cwd + '/' + candidate_name
		if not os.path.isdir(target_folder):
			os.makedirs(target_folder)
		tarfile = tarfile.open(folder_path + f)
		tarfile.extractall(target_folder + '/' + os.path.basename(f))










		
