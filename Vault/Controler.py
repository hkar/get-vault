__author__ = 'hkar'

from Vault import *
import Vault.Input
import Vault.Archive
import Vault.Crypto
import Vault.Storage
import Vault.Key


class basic(object):
    def __init__(self, config):
        self.config = config

        self.tmpdir = '/tmp/backup-' + get_random_string(20)
        self.tmp_archive = ''
        self.tmp_ecrypted = ''
        self.tmp_passwd = self.tmpdir + '-passwd.txt'
        self.tmp_passwd_encrypted = self.tmp_passwd + '.enc'
        self.password = get_random_string(64)

    def prepare(self):
        # create tmp dir

        os.mkdir(self.tmpdir)

        # prepare data
        for input_type, conf in self.config['input'].items():
            if input_type == 'mysql':
                Vault.Input.MysqlInput.prepare(self.tmpdir, conf)

        # create archive with files
        self.tmp_archive = self.tmpdir + Vault.Archive.ZipArchive.get_suffix()
        Vault.Archive.ZipArchive.pack(self.tmpdir, self.tmp_archive)

        # aes encrypt archive
        self.tmp_ecrypted = self.tmp_archive + '.aes'
        Vault.Crypto.AesSymmetric.encrypt(self.tmp_archive, self.tmp_ecrypted, self.password)

        # rsa encrypt password
        with open(self.tmp_passwd, 'w') as f:
            f.write(self.password)
            f.close()

        Vault.Crypto.RsaAsymmetric.encrypt(self.tmp_passwd, self.tmp_passwd_encrypted, Vault.Key.RsaKey.public())

        # remove unencrypted files
        #shutil.rmtree(self.tmpdir)
        for f in [self.tmp_archive, self.tmp_passwd]:
            os.remove(f)

    def upload(self):
        s3_config = self.config['storage']['s3']
        storage = Vault.Storage.S3Storage(s3_config['access_id'], s3_config['access_secret'], s3_config['bucket'], s3_config['endpoint'])

        storage.save("{prefix}-{time}{sym_suffix}".format(prefix=self.config['backup_prefix'], time=time.strftime('%d%m%y-%H%M'), sym_suffix='.enc'), self.tmp_passwd_encrypted)
        storage.save("{prefix}-{time}{sym_suffix}".format(prefix=self.config['backup_prefix'], time=time.strftime('%d%m%y-%H%M'), sym_suffix='.aes'), self.tmp_ecrypted)
