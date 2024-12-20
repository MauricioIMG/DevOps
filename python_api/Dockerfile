# Usa una imagen base específica de Python para garantizar reproducibilidad
FROM python:3.12.5-slim-bullseye

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /opt/python-api/

# Copia únicamente el archivo de dependencias primero para aprovechar la caché
COPY api/requirements.txt .

# Instala las dependencias del proyecto y limpia cachés para reducir el tamaño de la imagen
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente del proyecto al contenedor
COPY api/ .

# Expone el puerto 8001 para la API
EXPOSE 8001

# Configura el comando de inicio para ejecutar el servidor Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
