import os


EXE_ENV = os.environ.get('EXE_ENV', 'local')

from .base import *
exec 'from .{} import *'.format(EXE_ENV)