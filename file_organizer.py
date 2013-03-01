# data file organizer
# written in python

import ConfigParser
import shutil
import os
import tarfile

# define working path and resources

config = ConfigParser.RawConfigParser()
config.read('localconfig.conf')
root_dir = config.get('Pathes', 'root')
tar_dir = config.get('Pathes', 'tar')
unzip_dir = config.get('Pathes', 'unzip')
csv_dir = config.get('Pathes', 'csv')
merged_dir = config.get('Pathes', 'merged')

keywords = [ 'accel', 'audio', 'batt', 'cmpss', 'gps' ]

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

def CleanDir(unzip_dir, csv_dir):
	walker = os.walk(unzip_dir)
	for path, dirs, files in walker:
		for f in files:
			if os.path.splitext(f)[1] =='.csv':
				candidate = f.split('_')[2]
				if not os.path.isdir(csv_dir + candidate):
					os.makedirs(csv_dir + candidate)
				shutil.copyfile(path + '/' + f, csv_dir + candidate + '/' + os.path.basename(f))

def Merger(candidate, keyword, src_dir, tgt_dir):
	files_list = os.listdir(src_dir)
	fout_name = candidate + '_' + keyword + '.csv'
	fout_fullpath = tgt_dir + fout_name
	if os.path.isfile(fout_fullpath):
		os.remove(fout_fullpath)
	fout = open(fout_fullpath, 'a+')
	t = 1
	for path, dirs, files in os.walk(src_dir):
		for f in files:
			if os.path.splitext(f)[1] == '.csv' and f.split('_')[1] == keyword:
				lines = open(path + f, 'r')
				if t == 1:
					for line in lines:
						fout.write(line)
					t = 2
				else:
					lines.next()
					for line in lines:
						fout.write(line)
	fout.close()

def Trivial_Fixer(can, can_wrg, keyword, src_dir, tgt_dir):
	f_org_n = can + '_' + keyword + '.csv'
	f_app_n = can_wrg + '_' + keyword + '.csv'
	f_out_nf = tgt_dir + f_org_n
	f_org = open(src_dir + f_org_n, 'r')
	f_out = open(f_out_nf, 'a+')
	for line in f_org:
		f_out.write(line)
	f_org.close()
	f_app = open(src_dir + f_app_n, 'r')
	f_app.next()
	for line in f_app:
		f_out.write(line)
	f_app.close()
	f_out.close()

# ExtractFiles(tar_dir, unzip_dir)
# CleanDir(unzip_dir, csv_dir)

# Merge data according to categories

# candidates = os.listdir(csv_dir)

# for c in candidates:
# 	if os.path.isdir(csv_dir + c):
# 		for k in keywords:
# 			Merger(c, k, csv_dir + c + '/', merged_dir)
# 	else:
# 		continue

# fix problems with some person with different names

# cans = [ 'DAISEY', 'LILLY' ]
# cans_wrg = [ 'DAISY', 'LILY' ]
# for i in range(2):
# 	for kw in keywords:
# 		Trivial_Fixer(cans[i], cans_wrg[i], kw, merged_dir, root_dir)

print 'DONE'
		
