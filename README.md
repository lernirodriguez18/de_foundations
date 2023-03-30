# Trabajo Práctico Final Foundations

Bienvenido al TP Final de la sección Foundations del Módulo 1 de la Diplomatura en Cloud Data Engineering del ITBA.

En este trabajo práctico vas a poner en práctica los conocimientos adquiridos en: 

1. Bases de Datos Relacionales (PostgreSQL específicamente).
2. BASH y Linux Commandline.
3. Python 3.7+.
4. Docker.

## Ejercicios

### Ejercicio 1: Elección de dataset y preguntas

Elegir un dataset de la [wiki de PostgreSQL ](https://wiki.postgresql.org/wiki/Sample_Databases) u otra fuente que sea de interés para el alumno.

Crear un Pull Request con un archivo en [formato markdown](https://guides.github.com/features/mastering-markdown/) expliando el dataset elegido y  una breve descripción de al menos 4 preguntas de negocio que se podrían responder teniendo esos datos en una base de datos relacional de manera que sean consultables con lenguaje SQL.


## Ejercicio 2: Crear container de la DB

Crear un archivo de [docker-compose](https://docs.docker.com/compose/gettingstarted/) que cree un container de [Docker](https://docs.docker.com/get-started/) con una base de datos PostgreSQL con la versión 12.7.
Recomendamos usar la [imagen oficial de PostgreSQL](https://hub.docker.com/_/postgres) disponible en Docker Hub.
 
Se debe exponer el puerto estándar de esa base de datos para que pueda recibir conexiones desde la máquina donde se levante el container.


## Ejercicio 3: Script para creación de tablas

Crear un script de bash que ejecute uno o varios scripts SQL que creen las tablas de la base de datos en la base PostgreSQL creada en el container del ejercicio anterior.

Se deben solamente crear las tablas, primary keys, foreign keys y otras operaciones de [DDL](https://en.wikipedia.org/wiki/Data_definition_language) sin crear o insertar los datos. 


## Ejercicio 4: Popular la base de datos

Crear un script de Python que una vez que el container se encuentre funcionando y se hayan ejecutado todas las operaciones de DDL necesarias, popule la base de datos con el dataset elegido.

La base de datos debe quedar lista para recibir consultas. Durante la carga de información puede momentareamente remover cualquier constraint que no le permita insertar la información pero luego debe volverla a crear.

Este script debe ejecutarse dentro de un nuevo container de Docker mediante el comando `docker run`.

El container de Docker generado para no debe contener los datos crudos que se utilizarían para cargar la base.
Para pasar los archivos con los datos, se puede montar un volumen (argumento `-v` de `docker run`) o bien bajarlos directamente desde Internet usando alguna librería de Python (como `requests`).


## Ejercicio 5: Consultas a la base de datos

Escribir un script de Python que realice al menos 5 consultas SQL que puedan agregar valor al negocio y muestre por pantalla un reporte con los resultados.

Este script de reporting debe correrse mediante una imagen de Docker con `docker run` del mismo modo que el script del ejercicio 4.


## Ejercicio 6: Documentación y ejecución end2end

Agregue una sección al README.md comentando como resolvió los ejercicios, linkeando al archivo con la descripción del dataset y explicando como ejecutar un script de BASH para ejecutar todo el proceso end2end desde la creación del container, operaciones de DDL, carga de datos y consultas. Para esto crear el archivo de BASH correspondiente. 


## Resolucion del TP

1. Realice la descarga del dataset correspondiente. La explicacion esta en [Description_TP.md](Description_TP.md)
2. Configure un docker-compose donde:
    - Selecione la imagen de postgres 12.10
    - Configure las variables de entorno (user, pass y db_name)
    - Configure el puerto 5432, que es donde trabaja postgres
    - Estableci 2 volumenes. Uno para ejecutar la creacion de tablas y el otro para que persistan los datos
    - Configure una red, para luego poder conectarme desde el contenedor python que correré luego.
3. Configure un Dockerfile donde:
    - Seleccione la imagen de Python 3.9
    - Cargue todos los pkg necesarios para correr mis scrips (`requeriments.txt`) y luego los ejecute con un `pip install -r requeriments.txt`
4. Realice mi script en python utlizando Pandas y SQLAlchemy para poder llenar las tablas con el dataset
5. Realice mi script en python donde respondo las preguntas de negocio establecidas

El script [exec_tp_foundations.sh](exec_tp_foundations.sh) contiene todo lo necesario para hacer funcionar este proyecto
El contenido del script es el siguiente

- Creo mi imagen python3 `docker build -t python3 . `
- Inicializo mi docker-compose, donde se carga postgres `docker-compose up -d`
- Inicializo mi imagen de python3 y creo un volumen para copiar los archivos .py y el dataset `docker run -d --name upload_data -v "$PWD"/data:/usr/src/myapp -w /usr/src/myapp python3 sleep 1000 `
- Conecto mi contenedor de python a la red de postgres para poder comunicarlos `docker network connect tpf-foundations-lernirodriguez18_foundations_net upload_data`
- Ejecuto mi script de python para cargar las tablas de la db `docker exec -it upload_data bash -c "python3 upload_data.py"`
- Ejecuto mi script de python para responder las preguntas de negocio `docker exec -it upload_data bash -c "python3 consultas_negocio.py"`
