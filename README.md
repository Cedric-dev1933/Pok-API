# Pokédex com Flask e PokéAPI

Projeto web simples de uma Pokédex, desenvolvido em Python com Flask. O usuário digita o nome de um Pokémon em uma barra de busca e recebe informações como ID, altura, peso, tipos, habilidades e sprite frontal do Pokémon pesquisado.

## Tecnologias utilizadas

O projeto utiliza **Python** como linguagem principal, **Flask** como framework web para lidar com as rotas e renderização de templates, e a biblioteca **Requests** para realizar as chamadas HTTP à [PokéAPI](https://pokeapi.co/), uma API pública e gratuita com dados de todos os Pokémon. O front-end é feito com HTML puro, usando o sistema de templates **Jinja2** (integrado ao Flask) para exibir os dados dinamicamente na página.

## O que foi aprendido

Esse projeto foi desenvolvido como primeiro contato com consumo de APIs e desenvolvimento web com Python. Durante o processo, foram trabalhados os seguintes conceitos:

Como fazer requisições HTTP com a biblioteca Requests e interpretar o código de status da resposta. Como navegar pela estrutura de um JSON retornado por uma API, identificando dicionários aninhados e listas de objetos. Como usar o Flask para criar rotas que aceitam os métodos GET e POST, e como distinguir os dois dentro da mesma função. Como ler dados enviados por um formulário HTML usando `request.form`. Como processar e "limpar" os dados brutos da API antes de enviá-los ao template, montando dicionários customizados com apenas as informações relevantes. Como usar o Jinja2 para exibir dados dinâmicos no HTML, incluindo condicionais com `{% if %}` e laços com `{% for %}`.

## Como rodar localmente

Certifique-se de ter o Python instalado. Clone o repositório e, dentro da pasta do projeto, instale as dependências:

```bash
pip install flask requests
```

Em seguida, execute o servidor:

```bash
python Flask.py
```

Abra o navegador e acesse `localhost:5000`. Digite o nome de qualquer Pokémon na barra de busca e clique em Pesquisar.
