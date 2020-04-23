Title: Ambientes Virtuais com Python
Date: 2020-04-05 09:00
Modified: 2020-04-05 09:00
Category: Python
Tags: python, venv, virtualenv, environments
Slug: python-venv
Authors: Berg Paulo

A utilização de ambientes virtuais para aplicações em Python se tornou bastante utlizada por vários motivos, dentre eles isolar os pacotes da aplicação com os do pacotes do sistema.

Isso ajuda bastante trabalha em vários projetos usando as mesmas bibliotecas mas com versões diferentes, e também com ambientes em que não exista permissão para instalação dos pacotes como superusuário assim com o `venv` não há preocupação.

Existem algumas vantagens em utilizar o `venv` no lugar de outras bibliotecas, uma delas é que se trata um pacote do próprio `python3`, trazendo assim toda as facilidades de uma biblioteca padrão.

Caso tenha interesse em conhecer outras bibliotecas e suas diferenças no link abaixo temos uma explicação bacana sobre cada uma delas _em inglês_:
[https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)

### Instalando o pacote `venv`

Obs:
O `venv` funciona nas versões 2.7, 3.5, 3.6, 3.7.6 e 3.8 do Python.<br>
Neste post iremos usar a 3.x, padrão de vários sistemas operacionais como no Ubuntu e no Manjaro.

Instale o pacote `venv` com o `pip3`:

    :::bash
    sudo apt install python3-venv

Dentro do seu projeto use o comando `python -m venv .venv` para criar uma virtual environment:

    :::bash
    python -m venv .venv


Pronto instalação finalizada. Agora vamos aprender a usar o `venv` dentro do nosso projeto:

### Adicionando uma `venv` no seu projeto

Crie a pasta do seu projeto:

    :::bash
    mkdir nome_do_projeto


Entre na pasta do projeto:

    :::bash
    cd nome_do_projeto


Insira o seguinte comando para criar uma `venv` dentro do seu projeto:

    :::bash
    python -m venv .venv


Precisamos ativar a `venv` para que use a versão do python e pacotes apenas no seu projeto separando-os do seu sistema operacional:

    :::bash
    source .venv/bin/activate


O retorno será semelhante a esse:

    :::bash
    (.venv)bergpb@localhost


Para desativar a `venv` basta usar o seguinte comando:

    :::bash
    deactivate


Eu costumo adicionar o comando para ativar uma `venv` como alias no meu `.bashrc` desta forma, assim não preciso digitar o comando completo, apenas utilizo o alias `activate`:

    :::bash
    echo "alias activate='source .venv/bin/activate'" >> ~/.bashrc


Pronto agora você pode instalar pacotes sem se preocupar com conflitos em outros projetos.