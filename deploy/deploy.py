#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric import Connection
from invoke.exceptions import UnexpectedExit


print('Code For Curitiba - Sistema de deploy do projeto onibus-io-frontend\n')

connect_kwargs = {
    "key_filename": ["id_rsa"]
}

with Connection(host='jarvis.preludian.com.br', 
                user='preludian', 
                port=40022,
                connect_kwargs=connect_kwargs) as c:
    try:
        print ('Stopping containers and destroying images...')
        c.run('docker stop code4cwb-onibus-io-frontend-container && \
               docker rm code4cwb-onibus-io-frontend-container && \
               docker rmi code4cwb/onibus-io-frontend')
    except UnexpectedExit:
        print ('Delete deleting container not possible... Keep going')

    print('Running container...')
    c.run('docker run --restart=always -d --name code4cwb-onibus-io-frontend-container -m 128m -p 9001:80 code4cwb/onibus-io-frontend')

print('\nTerminado com sucesso')
