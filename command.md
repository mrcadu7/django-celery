pip freeze > requeriments.txt
chmod +x ./entrypoint.sh
docker-compose up -d --build
docker-exec -it django /bin/sh
./manage.py startapp taskapp
from newapp.tasks import tp1, tp2, tp3, tp4

# Agrupamento
task_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_group.apply_async()


# Encadeamento
task_chain = chain(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_chain.apply_async()


# Remove all docker
docker stop $(docker ps -aq) && docker rm $(docker ps -aq) && docker rmi $(docker images -aq)


from dcelery.celery_tasks.ex1_try_except import my task
from dcelery.celery_tasks.ex2_custom_task_class import my_task


tp1.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()