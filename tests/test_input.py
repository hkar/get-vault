__author__ = 'hkar'

import Vault.Input
from test_helpers import *


def test_mysql_prepare(tmpdir):
    tmpdir = str(tmpdir)

    for input_type, conf in config['input'].items():
        if input_type == 'mysql':
            result_files = Vault.Input.MysqlInput.prepare(tmpdir, conf)
            if len(result_files) == 0:
                assert False
            else:
                assert True