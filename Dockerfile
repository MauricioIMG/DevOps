# Usa imagen slim de Python para reducir tamaño
FROM python:3.12.5-slim

# Establece directorio de trabajo
WORKDIR /opt/python-api/

# Copia solo archivo dependencias (no código fuente completo)
COPY . .

# Instala dependencias de proyecto para aprovechar caché
RUN pip install -r requirements.txt

# Define variables de entorno para configuración de la aplicación
ENV MONGODB_HOST=mongodb
ENV MONGODB_PORT=27017

# Define punto de entrada de aplicación, indicando a Docker qué comando ejecutar
ENTRYPOINT ["uvicorn", "main:app"]

# Configura aplicación para que se ejecute en host 0.0.0.0 y en el puerto 8000.
CMD ["--host", "0.0.0.0", "--port", "8000"]