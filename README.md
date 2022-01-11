Set Up

Se inicio un proyecto de Django junto con una app del mismo llamada "apisAPP".
Se configuro Celery junto a RabbitMQ.
Se instalaron otras dependencias para el funcionamiento general como "request"

Encender el servidor:
    En la carpeta de apis ejecutar los siguientes comandos:
    pip install requirements.txt
    cd apis
    python manage.py runserver

Encender Celery:
    celery -A projectname worker1 -l INFO

    