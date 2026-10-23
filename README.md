# Магазин

Проект по девопсу. Простой сайт со списком товаров, товары можно добавлять. Фронт на vite, бэк на flask, база postgres, всё запускается в докере.

## Запуск

```
./start.sh
```

или то же самое руками:

```
docker compose up -d --build
```

Сайт открывается на http://localhost:8080. Остановить: `docker compose down`.

## Что где лежит

- `backend/` - бэкенд на flask и его Dockerfile
- `frontend/` - фронт и Dockerfile. Он multi-stage: сначала фронт собирается в образе node (`npm run build`), потом готовые файлы копируются в nginx
- `docker-compose.yml` - поднимает базу, бэк и фронт, все в одной сети `mynetwork`
- `push.sh` - собирает образы и заливает их в registry
- `docker-compose-remote.yml` - запуск на другой машине из образов в registry
- `ansible/` - плейбук для настройки сервера
- `practice/` - практики по докеру и ансиблу

## Registry

Нужно две машины. На первой запускаем registry и заливаем туда образы:

```
docker run -d -p 5000:5000 --restart always --name registry registry:2
./push.sh
curl http://localhost:5000/v2/_catalog
```

На второй машине докеру надо разрешить качать с нашего registry, потому что он работает без https. В `/etc/docker/daemon.json` пишем:

```
{ "insecure-registries": ["IP_первой_машины:5000"] }
```

и делаем `sudo systemctl restart docker` (плейбук ансибла это тоже делает). Потом в `docker-compose-remote.yml` меняем 192.168.0.10 на IP первой машины и запускаем:

```
docker compose -f docker-compose-remote.yml up -d
```

Образы скачаются из registry, на второй машине ничего не собирается.

## Ansible

В `ansible/inventory.ini` пишем IP своих машин, в `ansible/playbook.yml` адрес своего репозитория. Потом:

```
cd ansible
ansible-playbook playbook.yml
```

Плейбук ставит docker и git, настраивает git, создает ssh ключ (его выводит в консоль, ключ надо добавить в github) и скачивает проект в `/home/ubuntu/devops-project`.

## Версии

Стабильные версии помечены тегами в git, сейчас это `v1.0`. Образы в registry с тем же номером: `shop-backend:1.0`.

Чтобы выпустить новую версию, меняем `VERSION` в `push.sh` и номер версии у образов в `docker-compose-remote.yml`, потом:

```
git tag v1.1
git push origin main --tags
```
