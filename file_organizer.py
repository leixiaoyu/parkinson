# data file organizer
# written in python

import os
import tarfile

def extract(tar_url, extract_path='.'):
     print tar_url
     tar = tarfile.open(tar_url, 'r')
     for item in tar:
         tar.extract(item, extract_path)
         if item.name.find(".tgz") != -1 or item.name.find(".tar") != -1:
             extract(item.name, "./" + item.name[:item.name.rfind('/')])


cwd = os.getcwd()
print 'Current working directory: ' + cwd
folder_path = '/Users/xiaoyu/Documents/parkinson_data/MJFF-Data/'
files_full = os.listdir(folder_path)
for f in files_full:
	if len(f) > 9:
		candidate_name = f.split('_')[1]
		target_folder = cwd + '/' + candidate_name
		if not os.path.isdir(target_folder):
			os.makedirs(target_folder)
		tarfile = tarfile.open(folder_path + f)
		tarfile.extractall(target_folder + '/' + os.path.basename(f))










		
