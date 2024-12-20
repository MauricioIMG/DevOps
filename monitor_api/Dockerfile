FROM python:3.12-slim

# Directorio trabajo dentro del contenedor
WORKDIR /opt/monitor

# Copia código fuente y dependencias
COPY . /opt/monitor/

# Instala dependencias desde archivo requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Establece variable entorno para zona horaria (TZ) contenedor
ENV TZ=${TZ}

# Comando para ejecutar script monitoreo
CMD ["python", "monitor.py"]
