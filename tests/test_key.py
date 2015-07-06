__author__ = 'hkar'

import Vault.Key
from test_helpers import *


def test_rsa_exist():
    assert os.path.exists(Vault.Key.RsaKey.key_storage)

    assert not Vault.Key.RsaKey.exist()

    files = [Vault.Key.RsaKey.key_storage + Vault.Key.RsaKey.private_name, Vault.Key.RsaKey.key_storage + Vault.Key.RsaKey.public_name]
    for f in files:
        i = open(f, 'w')
        i.write(' ')
        i.close()

    assert Vault.Key.RsaKey.exist()

    for f in files:
        os.remove(f)

    assert not Vault.Key.RsaKey.exist()


def test_rsa_generate():
    assert not Vault.Key.RsaKey.exist()  # we need empty key folder, no overwriting..

    assert Vault.Key.RsaKey.generate()

    assert not Vault.Key.RsaKey.generate()

    Vault.Key.RsaKey.delete_keys()