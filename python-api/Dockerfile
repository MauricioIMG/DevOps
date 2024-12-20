# Usamos la imagen oficial de Python como base
FROM python:3.12-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /opt/python-api

# Copiamos los archivos del proyecto desde el directorio python-api
COPY . /opt/python-api/

# Instalamos las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /opt/python-api/requirements.txt

# Exponemos el puerto 8001 para acceder a la API
EXPOSE 8001

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

