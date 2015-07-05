__author__ = 'hkar'

from Vault import *


class BaseKey(object):
    __metaclass__ = abc.ABCMeta

    key_storage = 'keys/'

    @staticmethod
    def exist() -> bool:
        pass

    @staticmethod
    def public() -> str or False:
        pass

    @staticmethod
    def private() -> str or False:
        pass

    @staticmethod
    def generate(force=False) -> bool:
        pass


class RsaKey(BaseKey):
    private_name = 'rsa_backup_private.pem'
    public_name = 'rsa_backup_public.pem'

    @staticmethod
    def public() -> str or False:
        if RsaKey.exist():
            return RsaKey.key_storage + RsaKey.public_name
        else:
            return False

    @staticmethod
    def private() -> str or False:
        if RsaKey.exist():
            return RsaKey.key_storage + RsaKey.private_name
        else:
            return False

    @staticmethod
    def exist() -> bool:
        if os.path.exists(RsaKey.key_storage + RsaKey.private_name) and os.path.exists(RsaKey.key_storage + RsaKey.public_name):
            return True
        else:
            return False

    @staticmethod
    def generate(force=False) -> bool:
        if not force and RsaKey.exist():
            return False
        else:
            subprocess.check_output('openssl genrsa -out {private_path} 4096'.format(private_path=RsaKey.key_storage + RsaKey.private_name), shell=True)
            subprocess.check_output('openssl rsa -pubout -in {private_path} -out {public_path}'.format(private_path=RsaKey.key_storage + RsaKey.private_name,
                                                                                                       public_path=RsaKey.key_storage + RsaKey.public_name), shell=True)
            return True

    @staticmethod
    def delete_keys():
        files = [RsaKey.key_storage + RsaKey.private_name, RsaKey.key_storage + RsaKey.public_name]

        for f in files:
            os.remove(f)