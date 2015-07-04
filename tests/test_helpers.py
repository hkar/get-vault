__author__ = 'hkar'

import random
import string


def create_test_file(tmpdir):
    p = tmpdir.join("test_text.txt")
    text = get_random_string(1024)
    p.write(text)
    return p


def get_random_string(length:int=64) -> str:
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])
