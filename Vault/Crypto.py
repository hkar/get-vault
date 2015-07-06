__author__ = 'hkar'

from Vault import *


class BaseSymmetric(object):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    def encrypt(file_in, file_out, secret):
        pass

    @staticmethod
    def decrypt(file_in, file_out, secret):
        pass


class AesSymmetric(BaseSymmetric):
    @staticmethod
    def encrypt(file_in, file_out, secret):
        subprocess.check_output("openssl enc -in {file_in} -out {file_out} -e -aes256 -k {secret}".format(file_in=file_in, file_out=file_out, secret=secret), shell=True)

    @staticmethod
    def decrypt(file_in, file_out, secret):
        subprocess.check_output("openssl enc -in {file_in} -out {file_out} -d -aes256 -k {secret}".format(file_in=file_in, file_out=file_out, secret=secret), shell=True)


class BaseAsymmetric(BaseSymmetric):
    __metaclass__ = abc.ABCMeta


class RsaAsymmetric(BaseAsymmetric):
    @staticmethod
    def encrypt(file_in, file_out, pub_key):
        subprocess.check_output('openssl rsautl -encrypt -inkey {pub_key} -pubin -in {file_in} -out {file_out}'.format(pub_key=pub_key, file_in=file_in, file_out=file_out),
                                shell=True)

    @staticmethod
    def decrypt(file_in, file_out, private_key):
        subprocess.check_output('openssl rsautl -decrypt -inkey {private_key} -in {file_in} -out {file_out}'.format(private_key=private_key, file_in=file_in, file_out=file_out),
                                shell=True)
