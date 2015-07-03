__author__ = 'hkar'

from Vault import *


class BaseStorage(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, access_key, access_secret, bucket="", endpoint=""):
        self.endpoint = endpoint
        self.bucket = bucket
        self.access_secret = access_secret
        self.access_key = access_key

    @abc.abstractmethod
    def save(self, name, file): pass


class S3Storage(BaseStorage):
    def save(self, name, file):
        conn = tinys3.Connection(self.access_key, self.access_secret, tls=True, endpoint=self.endpoint)

        f = open(file, 'rb')
        r = conn.upload(name, f, self.bucket)

        if r.status_code == 201:
            return True
        else:
            raise CantUploadException()