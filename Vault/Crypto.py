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

