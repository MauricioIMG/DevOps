# Usamos la imagen oficial de Python como base
FROM python:3.12-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /opt/monitor

# Crear directorios necesarios (si no existen)
RUN mkdir -p /opt/monitor/logs

# Copiamos el código fuente y el archivo requirements.txt
COPY monitor.py /opt/monitor/monitor.py
COPY requirements.txt /opt/monitor/requirements.txt

# Instalamos las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /opt/monitor/requirements.txt

# Establecemos la variable de entorno para la zona horaria (TZ) del contenedor
ENV TZ=${TZ}

# Establecemos el punto de entrada para ejecutar el script de monitoreo
CMD ["python", "/opt/monitor/monitor.py"]
