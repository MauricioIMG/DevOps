# Proyecto Devops

Proyecto con API en python utilizando framework FastAPI, con Uvicorn, dockerizado.
Se presenta una guia de configuracion de proyecto y ejecucion de API:

## Configuración

1. **Clonar repositorio**

   ```Bash
   url_repositorio = https://github.com/MauricioIMG/DevOps.git
   git clone <url_repositorio>
   ```

2. **Construir imagen Docker**

   Construir imagen docker en root de proyecto: 

   ```Bash
   docker build -t python-api:v1.0.0 .
   ```

3. **Ejecutar contenedor**

   Ejecutar contenedor:

   ```bash
   docker run -p 8001:8001 python-api:v1.0.0
   ```

   Accede a la API: `http://localhost:8001`.

## Endpoints

#### 1. Documentación

- **Endpoint**: `/doc`
- **Uso con `curl`**:

  ```bash
  curl http://localhost:8001/
  ```

  `http://localhost:8001/docs/`, => Documentación generada por FastAPI.

#### 2. EndPoint: ordenar lista

- **Endpoint**: `/lista-ordenada`
- **Descripción**: Ordena lista numérica (str) y la devuelve ordenada
 con la hora actual del sistema.
- **Parámetro**: `lista-no-ordenada` de tipo str
- **Uso con `curl`**:

  ```bash
  curl "http://localhost:8001/lista-ordenada?lista-no-ordenada=[5,4,7,2,7,2]"
  ```

  **Ejemplo respuesta Endpoint**:

  ```json
  {
    "hora_sistema": "12:12:12",
    "lista_ordenada": [2, 2, 4, 5, 7, 7]
  }
  ```

#### 3. Endpoint: verificar estado

- **Endpoint**: `/healthcheck`
- **Descripción**: Verifica el estado de la API.
- **Uso con `curl`**:

  ```bash
  curl http://localhost:8001/healthcheck
  ```

  **Ejemplo Respuesta Endpoint**:

  ```text
  OK
  ```