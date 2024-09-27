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
  
## Integración de MongoDB

Se crea una red de MongoDb e integra al API.

1. **Crear red mongodb-net**

   ```Bash
   docker network create mongodb-net
   ```
   
2. **Correr el contenedor de MongoDB**

   ```Bash
   docker run -d --name mongodb --network mongodb-net -p 27017:27017 mongo:8.0.0-rc19-noble
   ```
    - **Descripción**: `-d` ejecuta contenedor en 2° plano, `--name mongodb` nombra el contenedor, `--network mongodb-net` asocia contenedor a red creada.   
   
3. **Correr el contenedor de MongoDB**

   ```Bash
   docker run -d --name python-api --network mongodb-net -p 8001:8001 python-api:v1.0.0
   ```

4. **Endpoint para probar el guardado de la lista-no-ordenada**
   - **Endpoint**: `/guardar-lista-ordenada`
   - **Descripción**:  Guarda una lista no ordenada en MongoDB y devuelve un
    mensaje con un ID único.
   - **Parámetro**: `lista-no-ordenada` de tipo str
   - **Uso con `curl`**:

     ```bash
     curl "http://localhost:8001/guardar-lista-no-ordenada?lista-no-ordenada=[5,4,7,2,7,2]"
     ```
     
     **Ejemplo respuesta Endpoint**:

     ```json
     {
      "msg":"La lista no ordenada fue guardada con el id: 577a9f55-2155-4069-85d9-bb44c1841297"
     }
     ```

## Docker-Compose

1. **Correr el proyecto**
   ```Bash
      docker-compose --env-file .env.demo --profile api --profile db up -d
      ```
       