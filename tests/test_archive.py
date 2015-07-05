__author__ = 'hkar'

from test_helpers import *
from Vault.Archive import ZipArchive
import os
import subprocess
import time


def test_zip(tmpdir):
    f = create_test_file(tmpdir)

    if not os.path.exists(str(f)):
        assert False

    tmpdir = str(tmpdir)

    archive_path = tmpdir + '/archive' + ZipArchive.get_suffix()
    test_file = tmpdir + '/test_file_backup.txt'

    ZipArchive.pack(tmpdir, archive_path)

    os.rename(str(f), test_file)

    ZipArchive.unpack(archive_path, tmpdir)

    assert True if os.path.exists(str(f)) else False
