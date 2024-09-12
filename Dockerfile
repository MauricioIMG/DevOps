# Usa imagen slim de Python para reducir tamaño
FROM python:3.12.5-slim

# Establece directorio de trabajo
WORKDIR /opt/python-api/

# Copia solo archivo dependencias (no código fuente completo)
COPY . /opt/python-api/

# Instala dependencias de proyecto para aprovechar caché
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . .

# Define el punto de entrada para iniciar el servidor
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
