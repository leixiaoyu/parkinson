# create configuration file
import ConfigParser

config = ConfigParser.RawConfigParser()
config.add_section('Pathes')
config.set('Pathes', 'root', '/Users/xiaoyu/Documents/parkinson_data/')
config.set('Pathes', 'tar', '/Users/xiaoyu/Documents/parkinson_data/MJFF-Data/')
config.set('Pathes', 'unzip', '/Users/xiaoyu/Documents/parkinson_data/processing/')
config.set('Pathes', 'csv', '/Users/xiaoyu/Documents/parkinson_data/csvs/')
config.set('Pathes', 'merged', '/Users/xiaoyu/Documents/parkinson_data/merged/')

with open('localconfig.conf', 'wb') as configfile:
	config.write(configfile)