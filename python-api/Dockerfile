# Imagen oficial de Python como base
FROM python:3.12-slim

# Establece directorio trabajo dentro contenedor
WORKDIR /opt/python-api

# Archivos del proyecto desde el directorio python-api
COPY . /opt/python-api/

# Instala dependencias desde requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /opt/python-api/requirements.txt

# Expone puerto 8001 para acceder API
EXPOSE 8001

# Ejecuta aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

