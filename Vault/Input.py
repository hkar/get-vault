__author__ = 'hkar'

from Vault import *


class BaseInput(object):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    def prepare(folder, config) -> list:
        pass


class MysqlInput(BaseInput):
    @staticmethod
    def prepare(folder, config) -> list:
        result_files = []
        for db in config['database']:
            dump_name = db + '.sql'
            subprocess.check_output(
                "mysqldump -h {host} -u {user} -p'{passwd}' -A -R -E --triggers --single-transaction > {file}".format(host=config['host'], user=config['user'],
                                                                                                                    passwd=config['passwd'], file=folder+'/'+dump_name), shell=True)
            result_files.append(dump_name)

        return result_files
