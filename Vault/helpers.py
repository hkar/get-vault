__author__ = 'hkar'

import random
import string

def get_random_string(length:int=64) -> str:
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])
