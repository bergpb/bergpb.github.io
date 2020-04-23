Title: PostgreSQL no Linux
Date: 2020-04-05 09:00
Modified: 2020-04-05 09:00
Category: Banco de Dados
Tags: postgresql, linux, database
Slug: instalacao-postgres-linux
Authors: Berg Paulo

"O PostgreSQL é um poderoso banco de dados objeto-relacional e de código aberto com mais de 30 anos de desenvolvimento."  
_Diretamente do site oficial._

O PostgreSQL é um dos bancos de dados relacionais mais utilizados até hoje, atualmente na versão 11.5 de acordo com o site oficial: [https://www.postgresql.org/](https://www.postgresql.org/)

### Instalação

Instalando os pacotes pelo `apt`:

    :::bash
    $ sudo apt install postgresql postgresql-contrib


Confira a versão instalada com o seguinte comando:

    :::bash
    $ psql --version
    > psql (PostgreSQL) 9.6.9


Entrando com permissões de superusuário:

    :::bash
    sudo -u postgres psql
    > psql (9.6.9)
    > Type "help" for help.

    > postgres=#


Agora iremos alterar a senha padrão do usuário `postgres`.

### Alterando senha do usuário `postgres`

Para alterar a senha do usuário padrão `postgres` devemos seguir os seguintes passos:  
Digite o seguinte comando para que possamos alterar o arquivo `pg_hba.conf`:  
_Obs: Pode variar de acordo com sua versão instalada._

    :::bash
    sudo nano /etc/postgresql/9.6/main/pg_hba.conf


Altere a seguinte linha:

    :::bash
    # De:
    # Database administrative login by Unix domain socket
    local   all             postgres                                peer
    # Para:
    # Database administrative login by Unix domain socket
    local   all             postgres                                md5


Reinicie o serviço com o seguinte comando:

    :::bash
    sudo service postgresql restart


Entre no console do `postgres` permissões de superusuário:

    :::bash
    sudo -u postgres psql


Altere sua senha com o comando:

    :::bash
    psql (9.6.9)
    Type "help" for help.

    postgres=#\password
    # digite sua nova senha:
    Enter new password:
    # digite novamente
    Enter it again:
    postgres=#


Pronto senha alterada.  
Você pode entrar no `psql` usando o comando `psql -U postgres -W` digitando sua nova senha.

### Comandos Básicos do `psql`

Iniciando serviço do `PostgreSQL`:

    :::bash
    sudo service postgresql start


Entrando no terminal do `psql` com sua senha do postgres:

    :::bash
    psql -U postgres -W
    > Password for user postgres:
    > postgres=#


Comandos do psql:

    :::bash
    \list # lista todas as databases no banco de dados
    \c nome_do_banco # realiza a conexão com o banco
    \dt # lista as tabelas no banco que está conectado
    \dn # mostra schemas criados
    \password # altera a senha para o usuário conectado
    \q # sai do console do psql


Podemos também executar comando sql dentro do `psql`:

    :::bash
    # criando um novo banco:
    postgres=#create database teste;
    CREATE DATABASE

    # conectando ao banco criado:
    postgres=#\c teste
    You are now connected to database "teste" as user "postgres".

    # criando uma nova tabela:
    postgres=#create table usuarios(nome varchar(20), idade int);
    CREATE TABLE

    # inserindo usuários no banco de dados:
    postgres=#insert into usuarios (nome, idade) values ('João', 22);
    INSERT 0 1

    # selecionando dados da tabela usuarios:
    nome | idade
    -----+------
    João |    22
    (1 row)
