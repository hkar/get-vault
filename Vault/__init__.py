__author__ = 'hkar'

import time
import abc
import tinys3
import subprocess

class CantUploadException(Exception): pass
