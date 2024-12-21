# librerías externas
import uuid
from fastapi import FastAPI, Query
from datetime import datetime

# librerias propias
from mongo_setup import get_mongo_db

app = FastAPI()

@app.get("/guardar-lista-no-ordenada")
def save_non_ordered_list(lista_no_ordenada: str = Query(
...,
        alias="lista-no-ordenada",
        description="Cadena de texto numérica separada por comas",
    )
) -> dict:
    """Endpoint para guardar una lista no ordenada en MongoDB y devuelve un
     mensaje con un ID único.

    Parámetro:
        lista_no_ordenada: lista_no_ordenada (str): Lista de números a ordenar.

    Returns:
        diccionario con mensaje con ID único de guardado de la lista.

    """
    try:
        lista_no_ordenada = [int(x) for x in lista_no_ordenada.strip("[]").split(",")]
    except ValueError:
        return {"error": "La lista debe contener solo números separados por comas."}

    tiempo = datetime.now().strftime("%Hh:%M:%S")

    id_unico = str(uuid.uuid4())

    data = {
        "id": id_unico,
        "lista_no_ordenada": lista_no_ordenada,
        "hora_sistema": tiempo
    }

    db = get_mongo_db()
    coleccion = db.listas_no_ordenadas
    coleccion.insert_one(data)

    respuesta = {"msg": f"La lista no ordenada fue guardada con el id: {id_unico}"}

    return respuesta

@app.get("/lista-ordenada")
def get_ordered_list(lista_no_ordenada: str = Query(
...,
        alias="lista-no-ordenada",
        description="Cadena de texto numérica separada por comas",
    )
) -> dict:
    """Endpoint para ordenar la lista de números.

    Parámetro:
        lista_no_ordenada (str): Lista de números a ordenar.

    Returns:
        diccionario con lista ordenada con hora actual del sistema.

    """
    lista_ordenada = sorted([int(x) for x in lista_no_ordenada.strip("[]").split(",")])

    tiempo = datetime.now().strftime("%Hh:%M:%S")

    respuesta = {
                "hora_sistema": tiempo,
                "lista_ordenada": lista_ordenada,
            }
    return respuesta


@app.get("/healthcheck")
def get_health_check() -> str:
    """Endpoint para verificar el estado del API.
    """
    return "OK"