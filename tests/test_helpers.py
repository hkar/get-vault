__author__ = 'hkar'

import os
import yaml
import pprint
from Vault.helpers import *

###
# overwrite local config variables for travis-ci
###

config_file = 'config.yaml'

if os.path.exists('test.'+config_file):
    config_file = 'test.'+config_file

with open(config_file, 'r') as stream:
    config = yaml.load(stream)

    if 'storage__s3__access_id' in os.environ:  # TODO: this is ugly...
        config['storage']['s3']['access_id'] = os.environ['storage__s3__access_id']

    if 'storage__s3__access_secret' in os.environ:
        config['storage']['s3']['access_secret'] = os.environ['storage__s3__access_secret']

pprint.pprint(config)

##
# helpers
##

def create_test_file(tmpdir, length=1024):
    p = tmpdir.join("test_text.txt")
    text = get_random_string(length)
    p.write(text)
    return p
