# 🐳TALLER DOCKER THE BRIDGE 🐳

> **En el taller de hoy vamos a ver lo básico que necesitamos saber para saber usar Docker en un entorno profesional sin tener conocimientos previos sobre la herramienta.**
> 

# 1. ¿Qué es Docker?

## Definición

> **Docker es un sistema operativo para contenedores. De manera similar a cómo una máquina virtual virtualiza (elimina la necesidad de administrar directamente) el hardware del servidor, los contenedores virtualizan el sistema operativo de un servidor.**
> 

## Características

- **MISMO ENTORNO**
    
    La idea de Docker es que te permite correr tu aplicación siempre en un mismo entorno. Esto quiere decir que todas las dependencias van a estar dentro de un mismo contenedor.
    
    Nosotros vamos a poder mover un contenedor entre una máquina u otra y nuestras dependencias siempre van a estar ahí dentro.
    
- **SANDBOX**
    
    Vamos a poder utilizar nuestro código independientemente del ordenador, sistema operativo o entorno en el que nos encontremos.
    
- **FÁCIL DE MOVER**
    
    Siempre funciona.
    

## Docker y Virtual Machine (VM)

Seguramente algunos de vosotros os estéis preguntando cuál es la diferencia entre Docker y una Virtual Machine.

![Untitled](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/Untitled.png)

- **Similitudes**
    
    La idea de una máquina virtual es que nuestras aplicaciones pueden correrse dentro de un sistema operativo y, para crear una nueva aplicación, vamos a tener que correr otra máquina virtual.
    
    Todo ello corre sobre un hipervisor y siempre sustentado por una infraestructura que puede ser, por ejemplo un servidor físico o una instancia en la nube.
    
- **Diferencias**
    
    La idea de Docker es que vamos a sacar una de esas capas de la ecuación y vamos a correr nuestra app junto con los archivos que necesita esa aplicación para correr.
    
    El kernel que corre cada uno de esos contenedores tiene un host compartido.
    
    Esto quiere decir que el host te da el kernel para que se corran mis aplicaciones.
    
    Esto quiere decir que un contenedor de Windows solo puede correr en un servidor que tenga un kernel de Windows.
    

**Imagino que ahora te estarás preguntando**

> ¿**Entonces cómo vamos a correr contenedores linux en una máquina con windows o con mac?**
> 

Cuando nosotros descargamos Docker Desktop, lo que estamos haciendo es crear una pequeño kernel que nos permite correr esos contenedores sobre ese kernel.

Simplemente esto nos viene bien a nivel de aprendizaje y desarrollo a pequeña escala, por lo que no debería preocuparnos el hecho de que tal vez nos tarde un poco más o ciertos procesos puedan ejecutarse más lentamente.

Lo ideal es correr un servidor linux con servidores de linux y así con cada sistema operativo.

![docker_etapas.png](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/docker_etapas.png)

# 2. Instalación de Docker

Para instalar docker:

```bash
https://www.docker.com/get-started
```

En función de nuestro sistema operativo, tendremos que descargar una versión de escritorio. Para los usuarios de Linux, entiendo que sabrán cómo apañárselas.

# 3. Funcionamiento de Docker

Básicamente Docker va a hacer lo siguiente:

> **Correr un contenedor a partir de una imagen**
> 

## **¿Qué es una imagen de Docker?**

> **Una imagen Docker es un archivo, compuesto por múltiples capas, que se utiliza para ejecutar código en un contenedor Docker. Estas imágenes son las plantillas base desde la que partimos ya sea para crear una nueva imagen o crear nuevos contenedores para ejecutar las aplicaciones.**
> 

**ESTRUCTURA**

- Sistema operativo.
    1. Ubuntu
    2. Debian
    3. Fedora
- Interpretes y compiladores
    1. GCC
    2. Java
    3. Python
- Servicios
    1. Apache
    2. Php
    3. Mysql
- App
    1. Dependencias
    2. Nuestro código

El código junto con las librerías y el sistema operativo son los elementos que componen nuestra imagen.

## ¿Cómo lanzamos esa imagen?

Para generar imágenes generamos lo que se conoce como Dockerfile

**DOCKERFILE**

> Archivo que contiene las instrucciones para crear nuestra imagen.
> 

Después de crear ese **Dockerfile**, corremos el comando que se llama `docker build` para generar esa imagen.

Si queremos correr esa imagen para crear este contenedor, utilizamos el comando `docker run` 

> **Probablemente, lo más interesante que tiene docker es que podemos correr un contenedor ejecutado por nosotros o bien podemos cargar una imagen que ha sido creada por otra persona.**
> 

Esto es genial porque nosotros podemos bajarnos una imagen ya creada y modificarla teniendo en cuenta las especificaciones de nuestra app.

### Ejemplo

Si queremos correr nuestro código Wordpress, en lugar de bajar una imagen de ubuntu, instalar todas las dependencias y demás, simplemente podemos bajarnos una imagen de wordpress y modificarla como queramos.

# Follow-Along

## AVISO PARA MAC 🍏

Es posible que tengáis un error a la hora de lanzar vuestros contenedores e imágenes por un tema de **PERMISOS.**

Para solucionarlo, tenéis que seguir los siguientes **PASOS:**

- **HABILITAR PERMISOS EN MAC**
    
    Abrir el menú 🍏 e ir a **"Preferencias del sistema"**
    
    Seleccionar **"Seguridad y Privacidad"**
    
    Hacer click en el **Candado** e introducir vuestra contraseña de usuario.
    
    En la barra desplegable de la izquierda, elegir **ACCESO TOTAL AL DISCO**
    
    Añadir una seleccionando el icono ➕
    
    Ir a Aplicaciones → Utilidades → Terminal
    
    **RELANZAR LA TERMINAL**
    
    [https://osxdaily.com/2018/10/09/fix-operation-not-permitted-terminal-error-macos/](https://osxdaily.com/2018/10/09/fix-operation-not-permitted-terminal-error-macos/)
    

## Correr una imagen

Vamos a correr una imagen a través de terminal

```bash
docker run postgres
```

**¿Cómo sé yo que hay una imagen que se llama *postgres?***

Esto lo tenemos en lo que se conoce como el registro de Docker.

Es el lugar en el que se hostean (es decir, se encuentran) estas imágenes.

```python
# Si no lo habéis hecho aún, tenéis que crearos vuestro usuario de Dockerhub
https://hub.docker.com/
```

Si aquí buscamos ***postgres***, vamos a tener todos los detalles sobre esta imagen, así como sus distintas versiones.

Si esta imagen no la tenemos previamente descargada, lo que se va a hacer es descargarla de Dockerhub, por eso veremos cómo se ejecutan varios comandos pull.

**Si queremos utilizar una versión concreta de una imagen, podemos añadirle un tag**

Si no especificamos, se va a descargar latest

Por ejemplo:

```python
# Es una buena práctica especificar la versión
docker run postgres:latest
```

Como véis, os habrá dado un error porque se exige que se añada un comando a correr.

En este caso, tenemos que mandarle una variable de entorno al contenedor para que se autoconfigure.

**NO OS PREOCUPÉIS. Si tenemos tiempo, lo veremos más adelante.**

**Por ahora, vamos a hacerle caso y a añadir esa línea de código.**

**FUNCIONA!!**

Como véis, yo no tengo descargado postgres en mi ordenador ni en ningún sitio. Simplemente creo esa imagen de postgres con la información necesaria para que mi app funcione.

Cuando se descarga una imagen, vamos a ver que cada una es un listado de capas, que vienen identificadas con su valor hash.

Nosotros podemos abrir una nueva terminal y correr una imagen de postgres con una versión distinta en otro contenedor dentro de un mismo servidor y no vamos a tener ningún problema.

## PostgreSQL + docker

Crear y lanzar contenedor postgreSQL

- Opción 1 - Te descarga imágen y carga el contenedor de una vez

```python
# Es una buena práctica especificar la versión
docker run --name postgres-db -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres
```

- Opción 2

```python
docker pull postgres

docker images

docker create -e  POSTGRES_PASSWORD=Admin_123 -e  POSTGRES_USER=postgres  -p 5010:5432  --name psqlserver ID_IMAGEN2 - Acceder por consola al contenedor postgresql
```

```python
docker exec -it 608 bash
```

Para poder ejecutar el motor de PSQL tenemos que cambiarnos de usuario, en este caso usaremos el usuario "postgres".

```python
 psql -U postgres
```

- Comandos SQL

Creación de la BBDD y tablas (hay que definir la bbdd y tablas del proyecto)

```sql
CREATE DATABASE bbdd;

-- Conectarse a la BBDD
\c bbdd

-- Authors

CREATE TABLE authors (
  id_author serial NOT NULL PRIMARY KEY,
  name varchar(45) NOT NULL,
  surname varchar(45) NOT NULL,
  email varchar(100) NOT NULL UNIQUE,
  image varchar(255)
);

-- Entries

CREATE TABLE entries (
  id_entry serial NOT NULL PRIMARY KEY,
  title varchar(100) NOT NULL,
  content text NOT NULL,
  date date DEFAULT CURRENT_DATE,
  id_author int,
  category varchar(15),
  FOREIGN KEY (id_author) REFERENCES authors(id_author)
);

-- Inserta varios autores

INSERT INTO authors(name,surname,email,image) VALUES
('Alejandru','Regex','alejandru@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/75.jpg'),
('Guillermu','Develawyer','develawyer@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/78.jpg'),
('Albertu','Henriques','albertu@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/80.jpg'),
('Alvaru','Arias','alvaru@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/70.jpg'),
('Birja','Ryvera','birja@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/72.jpg'),
('Muchelle','Ualis','muchelle@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/women/70.jpg'),
('Christianu','City','christianu@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/45.jpg');

-- Insertar una entry del blog

INSERT INTO entries(title,content,id_author,category) VALUES ('Nos vamos de pizzas al patio','The bridge invita a pizzas por reto de tripus','1','Sucesos');
```

Cheatsheet comandos por consola:

[https://www.postgresqltutorial.com/postgresql-cheat-sheet/](https://www.postgresqltutorial.com/postgresql-cheat-sheet/)

[https://www.valentinog.com/blog/psql/](https://www.valentinog.com/blog/psql/)

## Comandos más comunes en Docker

```python
# Solamente va a descargar las imágenes
docker pull 

# Para ver todas las imágenes que tenemos
docker images

# Para ver los contenedores que estamos corriendo en este momento
docker ps

# Para ver todos los conetendores que corrimos y los que están en ejecución
docker ps -a

# Ver los logs del contenedor
docker logs <container_id>
docker logs <container_nam e>

# Ejecuta un comando en un contenedor que ya está corriendo
docker exec -it <container_id> # crear una sesion interactiva. Con la t creamos una shell

# Para parar un contenedor
docker stop <container_id>

# Para correr un contenedor en segundo plano
docker run -d <image>

```
