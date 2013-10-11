# Reading settings from local_settings.yml

import os
import sys

# Should not be changed
ROOT_DIR = os.path.dirname(__file__)
#print(ROOT_DIR)

try:
	import yaml
	yaml_filename = 'local_settings.yml'
	default_yaml_path = os.path.join(ROOT_DIR,yaml_filename)
	if os.path.isfile(default_yaml_path):
		config = yaml.load(open(default_yaml_path,'r'))
		#print('Loaded config settings from {0}'.format(default_yaml_path))
	else:
		print('Can NOT load config settings from {0}'.format(default_yaml_path))
		sys.exit(1)
		
except ImportError,e:
	print(e)
	sys.exit(1)

DEBUG = config.get('debug',True)
MAX_PORT = config.get('max_port',65535)
WELL_KNOWN = config.get('well_known',1024)
