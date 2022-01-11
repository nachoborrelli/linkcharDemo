# Set Up Inicial
    Se inició un proyecto de Django junto con una app del mismo llamada "apisAPP".
    Se configuró Celery junto a RabbitMQ.
    Se instalaron otras dependencias para el funcionamiento general como "djangoRest" o "request"


# Encender el servidor:
    En la carpeta de apis ejecutar los siguientes comandos:
    ```pip install requirements.txt```
    ```cd apis```
    ```python manage.py runserver```

# Encender Celery:
    ```celery -A projectname worker1 -l INFO```


# Comentarios de desarrollo:
    La mayoría de los ejercicios consistían en consumir los datos de la base de datos, aplicando una query especifica, por esta razón,la mayoría de los ejercicios son similares en cuanto a código. Tuve que tener en cuenta el parámetro que llega por jsonBody y devolver un response acorde.
    Para todas las vistas se heredó de APIView, ya que esta brindaba un espacio acorde para lo solicitado, sin generar más recursos de los necesarios.
    
