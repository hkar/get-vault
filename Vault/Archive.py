__author__ = 'hkar'

from Vault import *


class BaseArchive(object):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    def get_suffix():
        return None

    @staticmethod
    def pack(files_in:list, file_out):
        pass

    @staticmethod
    def unpack(file_in, dir_out):
        pass


class ZipArchive(BaseArchive):
    @staticmethod
    def get_suffix():
        return ".zip"

    @staticmethod
    def pack(dir_in:str, file_out):
        subprocess.check_output("cd {dir_in} && zip {file_out} -r ./*".format(file_out=file_out, dir_in=dir_in), shell=True)

    @staticmethod
    def unpack(file_in, dir_out):
        subprocess.check_output("unzip -o {file_in} -d {dir_out}".format(file_in=file_in, dir_out=dir_out), shell=True)
