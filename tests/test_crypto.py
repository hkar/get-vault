__author__ = 'hkar'

import Vault.Crypto
import random
import string
import os


def test_aes(tmpdir):
    # make tmp text files
    p = tmpdir.join("test_text.txt")
    text = "The quick brown fox jumps over a lazy dog. („Rychlá hnědá liška skáče přes líného psa.“)"
    p.write(text)

    # define file names
    file_in = str(p)
    file_out = file_in + ".enc"

    # generate random secret
    secret = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(64)])

    # encrypt test file
    Vault.Crypto.AesSymmetric.encrypt(file_in, file_out, secret)

    # remove original test file
    os.remove(file_in)

    # decrypt test file
    Vault.Crypto.AesSymmetric.decrypt(file_out, file_in, secret)

    assert text == open(file_in, 'r').read()
