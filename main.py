# main working space
import ConfigParser
from packages.par_data import data_sampler as ds
from packages.par_file import file_organizer as fo
from packages.par_file import file_summerizer as fs
from packages import par_misc

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

# merge meta format data into one file
# fo.All_In_One(meta_dir, sample_dir, 'accel', candidates)

# convert file into meta neural format (change file name if necessary)
# for i in range(len(candidates)):
#     print i
#     f = merged_dir + candidates[i] + '_accel.csv'
#     fo.Convert_MetaFormat(f, meta_dir, patient[i], 100000 * (i + 1))

# summarize files in MetaNeural format into log file in log dir
# fs.File_Summary(meta_dir, log_dir, '')

# add up all the data of different keywords
people = candidates
fo.All_In_One(meta_dir, meta_dir, 'accel', people)

# sampling data into sample dir
# for i in range(len(candidates)):
#     print i
#     f = meta_dir + candidates[i] + '_accel_meta.csv'
#     ds.Sampling_without_Rep(f, sample_dir, 1000)

# convert CSV file into Meta file
# for i in range(len(candidates)):
#     print i
#     f = meta_dir + candidates[i] + '_accel_meta.csv'
#     fo.Csv_to_Meta(f, meta_dir)

# sampling data file in meta format
# f = sample_dir + 'total_records_accel.csv'
# ds.Sampling_without_Rep(f, sample_dir, 1000000)

# take first 1,000,000 row
# f = sample_dir + 'total_records_accel.csv'
# ds.Take_Rows(f, sample_dir, 6000000)

f = sample_dir + 'total_records_accel_sample_6m.csv'
ds.Take_Rows(f, sample_dir, 100)
