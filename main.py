# main working space
import ConfigParser
from packages import par_data
from packages import par_file
from packages import par_misc

config = ConfigParser.RawConfigParser()
config.read('localconfig.conf')
sample_dir = config.get('Pathes', 'sample')
merged_dir = config.get('Pathes', 'merged')
log_dir = config.get('Pathes', 'log')
test_dir = config.get('Pathes', 'test')
calculated_dir = config.get('Pathes', 'calculate')
candidates = config.get('Types', 'candidate').split(',')
keywords = config.get('Types', 'keyword').split(',')

# put code here #
