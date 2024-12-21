# Imagen oficial Python base
FROM python:3.12-slim

# Directorio trabajo dentro contenedor
WORKDIR /opt/monitor-api

# Directorios necesarios
RUN mkdir -p /opt/monitor-api/logs

# Script monitoreo y archivo requirements.txt
COPY monitor_script.py /opt/monitor-api/monitor_script.py
COPY requirements.txt /opt/monitor-api/requirements.txt

# Instala dependencias desde requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /opt/monitor-api/requirements.txt

# Establece variable entorno para zona horaria (TZ) contenedor
ENV TZ=${TZ}

# Establecemos punto entrada para ejecutar script monitoreo
CMD ["python", "/opt/monitor-api/monitor_script.py"]
