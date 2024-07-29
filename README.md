# Lumière

Lumière é uma newsletter de filmes criada com Flask, SQLite3, HTML e CSS. Este projeto permite aos usuários se inscreverem para receber atualizações periódicas sobre filmes diretamente em seus emails, com a opção de selecionar categorias extras de interesse no momento da inscrição.

## Descrição

Lumière é uma aplicação web que permite aos usuários se inscreverem em uma newsletter sobre filmes. O backend é desenvolvido em Flask, o banco de dados utilizado é o SQLite3, e o frontend é construído com HTML e CSS.

## Instalação

### Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado)

### Passos

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/lumiere.git
    cd lumiere
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate   # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Execute a aplicação:

    ```bash
    flask run
    ```

A aplicação estará disponível em `http://127.0.0.1:5000/`.

## Configuração

### Arquivo de Configuração

Configure as variáveis de ambiente necessárias no arquivo `.env`:

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

## Capturas de Tela

### Página Inicial

### Página de Inscrição

