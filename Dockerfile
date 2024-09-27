# Usa imagen slim de Python para reducir tamaño
FROM python:3.12.5-slim

# Establece directorio de trabajo
WORKDIR /opt/python-api/

# Copia solo archivo dependencias (no código fuente completo)
COPY . .

# Instala dependencias de proyecto para aprovechar caché
RUN pip install -r requirements.txt

EXPOSE 8001

# Configura aplicación para que se ejecute en host 0.0.0.0 y en el puerto 8001.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]