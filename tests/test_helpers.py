__author__ = 'hkar'

import random
import string
import os
import yaml
import pprint

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

def create_test_file(tmpdir):
    p = tmpdir.join("test_text.txt")
    text = get_random_string(1024)
    p.write(text)
    return p


def get_random_string(length:int=64) -> str:
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])
