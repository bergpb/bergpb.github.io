Title: Gerenciando dependências com o Yarn
Date: 2020-04-05 09:00
Modified: 2020-04-05 09:00
Category: Javascript
Tags: yarn, javascript
Slug: instalacao-yarn
Authors: Berg Paulo


O Yarn chegou e novembro de 2016 anunciado pelo Facebook sendo um gerenciador de pacotes mais rápido e seguro.
Hoje, tornou-se uma grande ferramenta em projetos escritos em Javascript.
Iremos aprender como instalar e utilizar alguns dos comandos disponíveis do `yarn`.

### Instalação

Adicione o yarn em seu repositório de pacotes no Ubuntu:

    :::bash
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

Após adicionar atualize os pacotes e instale o `yarn`:

    :::bash
    sudo apt update && sudo apt install yarn

Obs: Caso tenha realizado a instalação do node com `nvm`, use o seguinte comando:

    :::bash
    sudo apt install --no-install-recommends yarn

Para instalação no Manjaro, apenas execute o seguinte comando:

    :::bash
    sudo pacman -S yarn

+ Principais comandos do Yarn:
  + `yarn init` -- cria o arquivo package.json com suas principais configurações
  + `yarn add` -- adiciona o pacote para uso em seu projeto
  + `yarn install` ou simplesmente `yarn` -- instala as depedências definidas no `package.json`
  + `yarn remove` -- remove um pacote do projeto
  
Aqui alguns comandos para quem já está bastante familiarizado com o `npm`:

NPM | Yarn | Descrição
--- | ---- | -------- 
npm init | yarn init | Inicia um projeto
npm run | yarn run | Executando um projeto
npm install | yarn install ou yarn | Instalando pacotes do package.json
npm install [package] --save | yarn add [package] | Instalando pacote e salvando no package.json
npm install -g [package] | yarn global add [package] --prefix /usr/local | Instalando pacote globalmente
npm list -g --depth 0 | yarn global list | Listando pacotes globais
rm -rf node_modules && npm install | yarn upgrade | Atualizando pacotes
npm uninstall [package] | yarn remove [package] | Removendo pacotes

*** Fontes: ***  
[https://yarnpkg.com](https://yarnpkg.com)  
[https://yarnpkg.com/lang/en/docs/install/#debian-stable](https://yarnpkg.com/lang/en/docs/install/#debian-stable)