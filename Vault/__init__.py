__author__ = 'hkar'

import time
import abc
import tinys3
import subprocess
import os

class CantUploadException(Exception): pass
