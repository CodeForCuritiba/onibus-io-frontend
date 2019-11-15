# Onibus IO - Frontend

[![Build Status](https://travis-ci.org/CodeForCuritiba/onibus-io-frontend.svg?branch=master)](https://travis-ci.org/CodeForCuritiba/onibus-io-frontend)
Projeto frontend do Onibus IO; Montado em cima do vuejs e vuetify;

## Trabalhando no projeto

### Via fácil - Usando Docker

Não é necessário instalar nenhum software além do Docker. Se você tiver o Docker instalado no seu computador, basta rodar o seguinte comando.

    $ cd frontend;
    $ docker run -v $(pwd):/app -w /app -it --rm -p 8080:8080 node:13-alpine npm install && npm run serve

O comando é grande, mas o que ele faz?

* Roda o comando do docker usando:
  * roda o container;
  * monta a pasta atual (frontend) dentro da pasta /app dentro do container;
  * entra dentro da pasta /app de dentro do container;
  * entra em modo interativo (-it), removendo o container ao sair (--rm)
  * mapeia a porta 8080 do container no host 8080
  * depois roda o comando `npm install && npm run serve`

Para fechar o container, basta usar a sequencia de teclas `ctrl + c`.

### Usando o node instalado na sua máquina

Supondo que há uma instalação do node no seu computador, faça:

    $ cd frontend;
    $ npm install;
    $ npm run serve;


## Contribuindo

Para contribuir no projeto, clone-o, crie uma branch e depois faça um Pull request. Usamos o Github flow. [](https://guides.github.com/introduction/flow/).
Em caso de dúvidas, abra um issue nesse repositório.
