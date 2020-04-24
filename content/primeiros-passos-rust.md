Title: Primeiros passos com Rust
Date: 2020-04-23 00:00
Modified: 2020-04-23 00:00
Category: Programação
Tags: rust
Slug: primeiros-passos-rust
Status: published

_“Rust is a systems programming language focused on three goals: safety, speed, and concurrency.”_  
_Rust Documentation_

Iniciei meus estudos com a linguagem recentemente, e já me sinto bem entusiasmado em continuar prosseguindo com a linguagem.  
Mas porque o interesse em estudar Rust? Temos comunidades bem ativas aqui no Brasil, dispõe de uma ótima documentação e pela sua utilização em grandes projetos de empresas como Mozilla e Microsoft.

O Rust é uma linguagem compilada e multiparadigma, e trouxe várias coisas boas de outras linguagens.  
Algumas merecem ser citadas:

 - Modelos de Abstração de Máquina - C
 - Bindings Opcionais - Swift
 - Programação Funcional - Haskell, OCaml, F#
 - Passagem de Mensagens e Falhas em Threads: Erlang

Um dos pontos fortes da linguagem é seu compilador que traz ao usuário uma experiência incrível com relação a outras linguagens mas isso é assunto pra outro post.

Para iniciar com a linguagem é necessário a instalação de algumas ferramentas como:

 - `rustc` - Compilador do Rust
 - `cargo` - Gerenciador de pacotes do Rust
 - `clippy` - Linter do Rust

Para a instação destas ferramentas podemos utilizar o `rustup`, que vai deixar nosso ambiente pronto para começar com a linguagem.

Instalação do `rustup` para Linux e Mac:

    :::bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

Para Windows:
Faça o download do arquivo `rustup-init.exe` em [www.rustup.rs](www.rustup.rs) e execute.

Após a instalação você verá algo parecido no seu terminal:

    :::bash
    stable installed - rustc 1.43.0 (4fb7144ed 2020-04-20)
    Rust is installed now. Great!


Para verificar a instalação iremos executar o seguinte comando:

    :::bash
    rustc --version


Agora vamos ao famoso Hello World:

Crie um arquivo com o nome `hello_world.rs`,  
Insira o seguinte conteúdo no mesmo:

    :::rust
    fn main() {
        println!("Hello World")
    }

Obs:  
Rust trabalha com extensões de arquivo `.rs` e segue o `snake_case`.  
`fn` significa que estamos definindo uma função, e o `main` é o início de todo programa escrito em Rust.

Logo em seguida, salve o arquivo.  
Compile o mesmo com o comando `rustc hello_word.rs`.  
E execute o binário gerado com `./hello_world` (Linux ou Mac) ou `file.exe` (Windows)

    :::bash
    ❯ ./hello_world
    Hello World

Bem esse foi meu primeiro post falando sobre Rust, irei continuar progredindo com meus estudos na linguagem e irei postando as novidades por aqui.

Até o próximo post.


Alguns links interessantes:

 - Learning Rust: [https://learning-rust.github.io](https://learning-rust.github.io)
 - Rust Playgroud - [https://play.rust-lang.org/](https://play.rust-lang.org/)
 - rustup - [https://rustup.rs/](https://rustup.rs/)

