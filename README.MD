## Como Instalar

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
