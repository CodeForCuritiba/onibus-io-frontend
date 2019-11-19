#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric import Connection


print('Code For Curitiba - Sistema de deploy do projeto onibus-io-frontend\n')

connect_kwargs = {
    "key_filename": ["id_rsa"]
}

with Connection(host='jarvis.preludian.com.br', 
                user='preludian', 
                port=40022,
                connect_kwargs=connect_kwargs) as c:
    c.run('docker ps -a')
    c.run('docker images')
    c.run('docker pull code4cwb/onibus-io-frontend:latest')

print('\nTerminado com sucesso')
