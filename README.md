Online store project. Django-based. 

#Start  with docker (development):
### containers:  django + celery_worker + celery_flower + rabbitmq + postgresql + nginx + traefik
 
 - sudo docker-compose -f docker-compose.local.yml up --build
 
 
#Start with conda env and run rabbitmq as docker container (development):
### run rabbitmq as docker container:
- sudo docker-compose -f docker-compose.rabbitmq.yml up --build

### run celery worker in new shell:
-  conda activate env_38_online_shop
-  celery -A online_shop worker -l info
### run django_app in new shell:
-  python manage.py runserver

### now app is up at localhost:8000