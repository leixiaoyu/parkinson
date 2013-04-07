# main working space
import ConfigParser
# from packages import par_data
from packages.par_file import file_organizer as fo
# from packages.par_file import file_summerizer as fs
# from packages import par_misc

config = ConfigParser.RawConfigParser()
config.read('localconfig.conf')
sample_dir = config.get('Pathes', 'sample')
merged_dir = config.get('Pathes', 'merged')
log_dir = config.get('Pathes', 'log')
test_dir = config.get('Pathes', 'test')
calculated_dir = config.get('Pathes', 'calculate')
meta_dir = config.get('Pathes', 'meta')
candidates = config.get('Types', 'candidate').split(',')
patient = config.get('Types', 'patient').split(',')
keywords = config.get('Types', 'keyword').split(',')

# put code here #

# convert file into meta neural format (change file name if necessary)
# for i in range(len(candidates)):
#     print i
#     f = merged_dir + candidates[i] + '_accel.csv'
#     fo.Convert_MetaFormat(f, meta_dir, patient[i], 100000 * (i + 1))

# summarize files in MetaNeural format into log file in log dir
# fs.File_Summary(meta_dir, log_dir, '')

# add up all the data of different keywords
people = candidates
fo.all_in_one(meta_dir, meta_dir, 'accel', people)
