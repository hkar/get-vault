__author__ = 'hkar'

import Vault.Crypto
import Vault.Key
from test_helpers import *
import os


def test_aes(tmpdir):
    # make tmp text files
    f = create_test_file(tmpdir)

    text = str(f.read())

    # define file names
    file_in = str(f)
    file_out = file_in + ".enc"

    # generate random secret
    secret = get_random_string()

    # encrypt test file
    Vault.Crypto.AesSymmetric.encrypt(file_in, file_out, secret)

    # remove original test file
    os.remove(file_in)

    # decrypt test file
    Vault.Crypto.AesSymmetric.decrypt(file_out, file_in, secret)

    assert text == open(file_in, 'r').read()


def test_rsa(tmpdir):
    # make tmp text files
    f = create_test_file(tmpdir, length=64)

    text = str(f.read())

    # define file names
    file_in = str(f)
    file_out = file_in + ".enc"

    # generate keys
    Vault.Key.RsaKey.generate()

    # encrypt test file
    Vault.Crypto.RsaAsymmetric.encrypt(file_in, file_out, Vault.Key.RsaKey.public())

    # remove original test file
    os.remove(file_in)

    # decrypt test file
    Vault.Crypto.RsaAsymmetric.decrypt(file_out, file_in, Vault.Key.RsaKey.private())

    Vault.Key.RsaKey.delete_keys()

    assert text == open(file_in, 'r').read()