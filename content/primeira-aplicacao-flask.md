Title: Sua Primeira Aplicação com Flask
Date: 2020-04-05 09:00
Modified: 2020-04-05 09:00
Category: Flask
Tags: flask, python, microframework
Slug: primeira-aplicacao-flask
Authors: Berg Paulo


O Flask é um dos microframeworks mais utilizados na linguagem Python, por _"oferecer sugestões e não impõe qualquer dependência ou layout, dando assim liberdade ao desenvolvedor para escolher ferramentas e bibliotecas que desejar"_, além ser simples e prático de inicar uma aplicação como veremos abaixo:

Aviso:  
Obs: Tenha o `python3` e o `pip` instalados em seu SO.

### Iniciando aplicação

Vamos criar uma pasta para nosso projeto, criar uma `venv` e instalar o `flask`:

Criando uma pasta:

    :::bash
    mkdir primeira_aplicacao_flask

Entrando na pasta:

    :::bash
    cd primeira_aplicacao_flask

Agora vamos criar a nossa `venv`:

    :::bash
    python -m venv .venv

Vamos ativar a `venv`:

    :::bash
    source .venv/bin/activate

E instalar `flask` com o `pip`:

    :::bash
    pip3 install flask

Após isso já podemos criar nosso arquivo e iniciar nossa aplicação:

Cria um novo arquivo através do terminal:

    :::bash
    touch app.py

Usando alguma IDE de sua preferência ou o próprio `vim` ou `nano`, abra o arquivo criado no anteriormente e insira o seguinte conteúdo:

    :::python
    from flask import Flask

    def create_app():
        app = Flask(__name__)

        @app.route('/')
        def hello():
          return 'Hello World'

        return app


Devemos esportar as serguintes variáveis de ambiente para o Flask inicie a aplicação corretamente:

    :::bash
    export FLASK_ENV=development
    export FLASK_APP=app.py

Agora vamos servir nossa aplicação para que possamos ver seu retorno no browser.

    :::bash
    flask run

Teremos um retorno semelhante a esse:

    :::bash
     * Serving Flask app "app.py" (lazy loading)
     * Environment: development
     * Debug mode: on
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 123-456-789

Podemos acessar a aplicação através da url [http://localhost:5000](http://localhost:5000).

Agora você já pode se considerar um desenvolvendor iniciante com micro-framework Flask.<br>
Ainda tem bastante conteúdo sobre Flask para postar então fique ligado e até o próximo post.
