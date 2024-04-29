## Descrição do Projeto

Projeto construído com o intuito de realizar a geração de nuvens de palavras utilizando como bases de dados vídeos no youtube de canais de direita e de canais de esquerda, com o fim de obter uma visualização 
que mostrasse os termos mais frequentemente utilizados nos títulos dos videos e a partir disso identificar caracteríticas do discurso de ambos os espectros políticos.


## Como Executar

### Docker
Requisitos:

 - Docker
 - Docker-compose

Execute os seguintes comandos:

    docker-compose build
    docker-compose up --detach

Uma vez que o servidor local tenha iniciado, acesse http://127.0.0.1:8050/
### Local
Requisitos:

 - Python
 - Poetry

Execute os seguintes comandos:

   `poetry install`

   `poetry shell`

   `python app.py` ou `poetry run python app.py`

Uma vez que o servidor local tenha iniciado, acesse http://127.0.0.1:8050/
