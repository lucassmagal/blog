# -*- coding: utf-8 -*-
import os
from fabric.api import local, lcd
import glob
from datetime import date


def build():
    """Compila o site em arquivos estáticos,
    configura todo o conteúdo no output/, realiza
    um commit e faz push pro heroku
    """
    if not os.path.exists('output'):
        print ('Diretorio /output/ não existe! '
               'Você deve criá-lo antes, inclusive '
               'com um repositório git conectado '
               'ao heroku')
        raise RuntimeError

    local('python app.py build')

    for path in glob.glob('to_output/*'):
        local('cp %s output' % path)

    with lcd('output'):
        commit_message = "DEPLOY %s" % date.today().strftime("%Y_%m_%d")

        local('git add .')
        local('git commit -m "%s"' % commit_message)

        local('git push heroku master')
