from __future__ import with_statement
from fabric.api import local,run,cd, env
from settings_local import HOSTS

env.hosts = HOSTS
prefix = '/var/www/meako/data/'

def deploy():
    local('git push deploy master')
    with cd('%slpftv.git' % prefix):
        run('git checkout -f')
        run('git checkout-index -f -a --prefix=%swww/lpftv/' % prefix)
        run('cp -rf %swww/lpftv/lpftv/static %swww/lpftv.com/' %(prefix,prefix))
    run('touch %swww/lpftv/lpftv/lpftv.wsgi' % prefix)

     
