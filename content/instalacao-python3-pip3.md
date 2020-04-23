Title: python3 e pip3
Date: 2020-04-05 09:00
Modified: 2020-04-05 09:00
Category: Linguagem
Tags: python, pip
Slug: instalacao-python-pip
Authors: Berg Paulo


A instalação do `python3` e `pip3` se tornaram itens indispensáveis para muitos ambientes atuais de desenvolvimento.

A versão 2.7 do Python ainda é bastante utilizada mas será descontinuada em 2020 (o countdown pode ser conferido neste site [https://pythonclock.org](https://pythonclock.org)), e programas escritos com ele serão considerados obsoletos.  
Então comece a usa o `python3` em seus projeto e evite problemas futuros.

Caso você use o Manjaro (>18.x) ou Ubuntu (>18.x) não terá problemas com o mesmo pois o sistema já vem com `python3`, inclusive no Manjaro temos a versão `3.8.1`. 

Realizando a instalação:

Instalando os pacotes `python3` e `pip3` pelo apt:

    :::bash
    sudo apt install python3 python3-pip

Para conferir a versão do `python`:

    :::bash
    python3 --version

Para conferir a versão do `pip`:

    :::bash
    pip3 --version


Vamos entrar no console do `python`:

    :::bash
    python

E executar o famoso 'hello world':

    :::python
    # digite o texto abaixo e aperte enter:
    print('hello world')
    # saída no console:
    hello world