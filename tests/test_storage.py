__author__ = 'hkar'

import Vault.Storage
from test_helpers import *


def test_s3(tmpdir):
    s3_config = config['storage']['s3']
    storage = Vault.Storage.S3Storage(s3_config['access_id'], s3_config['access_secret'], s3_config['bucket'], s3_config['endpoint'])

    print(s3_config)

    f = create_test_file(tmpdir)

    storage.save("test.txt", str(f))

    assert True

