import sys,os

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

# Adding modules directory to python path
sys.path.insert(0, PROJECT_ROOT)

activate_this = '/var/www/meako/data/virtualenvs/myname/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from myname import app as application
