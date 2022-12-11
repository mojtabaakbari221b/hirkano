### RUN THIS COMMANDS ON ROOT DIRECTRORY OF PROJECT

## START PROJECT :
```
$ docker volume create mahpen_static_volume
$ docker volume create mahpen_media_volume
$ docker volume create mahpen_postgresql_volume
```
```
$ docker network create mahpen_network
```
```
$ docker-compose build
$ docker-compose up -d
```
```
$ docker exec -it mahpen python manage.py createsuperuser
```
## UPDATE PROJECT :
```
$ docker-compose down
$ docker-compose build (IF IMAGES ARE CHANGED)
$ docker-compose up -d
```

## UPDATE DATABASE IF MODELS ARE CHANGED
```
$ docker exec -it mahpen python manage.py makemigrations
$ docker exec -it mahpen python manage.py migrate
```