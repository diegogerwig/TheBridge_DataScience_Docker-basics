# Imagen base
FROM python:3.11-alpine

# Creamos una carpeta
RUN mkdir /src

# La establecemos como directorio de trabajo
WORKDIR /src

# Añadimos el contenido de src a src
ADD ./src /src

# Instalamos las dependencias de python
RUN pip install -r requirements.txt

# Ejecutamos el comando para lanzar la API
CMD ["python", "app.py"]

# Exponemos el puerto del backend
EXPOSE 5000