### RUN THIS COMMANDS ON ROOT DIRECTRORY OF PROJECT

## START PROJECT :
```
$ docker volume create hirkano_static_volume
$ docker volume create hirkano_media_volume
```
```
$ docker network create hirkano_network
```
```
$ docker-compose build
$ docker-compose up -d
```
```
$ docker exec -it hirkano python manage.py createsuperuser
```
## UPDATE PROJECT :
```
$ docker-compose down
$ docker-compose build (IF IMAGES ARE CHANGED)
$ docker-compose up -d
```

## UPDATE DATABASE IF MODELS ARE CHANGED
```
$ docker exec -it hirkano python manage.py makemigrations
$ docker exec -it hirkano python manage.py migrate
```