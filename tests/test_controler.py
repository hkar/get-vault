__author__ = 'hkar'

from test_helpers import *
import Vault.Controler
import Vault.Key

def test_simple():
    Vault.Key.RsaKey.generate()

    controler = Vault.Controler.basic(config)
    controler.prepare()
    controler.upload()

    Vault.Key.RsaKey.delete_keys()

    assert True