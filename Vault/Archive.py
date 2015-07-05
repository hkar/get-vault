__author__ = 'hkar'

from Vault import *


class BaseArchive(object):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    def pack(files_in:list, file_out):
        pass

    @staticmethod
    def unpack(file_in, dir_out):
        pass


class TargzArchive(BaseArchive):
    @staticmethod
    def pack(files_in:list, file_out):
        pass

    @staticmethod
    def unpack(file_in, dir_out):
        pass
