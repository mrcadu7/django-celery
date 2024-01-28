pip freeze > requeriments.txt
chmod +x ./entrypoint.sh
docker-compose up -d --build
docker-exec -it django /bin/sh
./manage.py startapp taskapp