# Практики

## Docker

- `01-image-and-container` - загрузка образа и создание контейнера
- `02-container-interaction` - взаимодействие с контейнером
- `03-flask-webapp` - контейнер с веб-приложением на flask
- `04-multi-stage` - сборка multi-stage
- `05-volume-mysql` - docker volume на примере mysql
- `06-network-bridge` - два контейнера в одной сети (nginx и flask)

В каждой папке файлы из практики и `commands.txt` с командами, которые выполнялись.

В практике с сетью пришлось сделать свою сеть через `docker network create`, в стандартной bridge контейнеры не видят друг друга по имени. И в Dockerfile там файл `flask_app.py`, а не `app.py`.

## Ansible

Все 17 практик делались в одной папке `ansible/`, как в методичке: `inventory.ini`, `ansible.cfg`, плейбуки, роль `myRole`, `group_vars`, `host_vars`. Практики 15 и 16 в `jinja_lesson/` и `vault_lesson.yml`, 17 в `web_service/`.

Пароль Ansible Vault хранится только локально в исключённом из Git файле `.vault_pass`. Для разовой проверки без файла можно использовать `ansible-vault view secret_vars.yml --ask-vault-pass`.
