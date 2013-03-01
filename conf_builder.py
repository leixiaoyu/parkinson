# create configuration file
import ConfigParser

config = ConfigParser.RawConfigParser()
config.add_section('Pathes')
config.add_section('Types')
config.set('Pathes', 'root', '/Users/xiaoyu/Documents/parkinson_data/')
config.set('Pathes', 'tar', '/Users/xiaoyu/Documents/parkinson_data/MJFF-Data/')
config.set('Pathes', 'unzip', '/Users/xiaoyu/Documents/parkinson_data/processing/')
config.set('Pathes', 'csv', '/Users/xiaoyu/Documents/parkinson_data/csvs/')
config.set('Pathes', 'merged', '/Users/xiaoyu/Documents/parkinson_data/merged/')
config.set('Pathes', 'log', '/Users/xiaoyu/Documents/parkinson_data/logs/')
config.set('Pathes', 'test', '/Users/xiaoyu/Documents/parkinson_data/test/')
config.set('Pathes', 'sample', '/Users/xiaoyu/Documents/parkinson_data/sample/')
config.set('Types', 'candidate', 'APPLE,CHERRY,CROCUS,DAFODIL,DAISEY,FLOX,IRIS,LILLY,MAPLE,ORANGE,ORCHID,PEONY,ROSE,SUNFLOWER,SWEETPEA,TESTCLIQ,VIOLET')
config.set('Types', 'keyword', 'accel,audio,batt,cmpss,gps')

with open('localconfig.conf', 'wb') as configfile:
	config.write(configfile)