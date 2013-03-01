# data sampler

import ConfigParser
import os
import random

config = ConfigParser.RawConfigParser()
config.read('localconfig.conf')
sample_dir = config.get('Pathes', 'sample')
merged_dir = config.get('Pathes', 'merged')
candidates = config.get('Types', 'candidate').split(',')
keywords = config.get('Types', 'keyword').split(',')

def File_Len(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

def Sampler(candidate, keyword, src_dir, tgt_dir):
	src_file = src_dir + candidate + '_' + keyword + '.csv'
	length = File_Len(src_file)
	used_num = [ 0 ]
	for i in range(100):
		ran = random.randint(1, length)
		while ran in used_num:
			ran = random.randint(1, length)
		used_num.append(ran)
	used_num.sort()
	fout_path = tgt_dir + candidate + '_' + keyword + '_sample.csv'
	fout = open(fout_path, 'w')
	with open(src_file, 'r') as fin:
		for i, line in enumerate(fin):
			if i in used_num:
				fout.write(line)
	fout.close()

print candidates
print keywords

for c in candidates:
	for kw in keywords:
		Sampler(c, kw, merged_dir, sample_dir)

print 'DONE'

