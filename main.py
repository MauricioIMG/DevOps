from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI()


@app.get("/lista-ordenada")
def get_ordered_list(lista_no_ordenada: str = Query(
...,
        alias="lista-no-ordenada",
        description="Cadena de texto numérica separada por comas",
    )
):
    """
    Endpoint para ordenar la lista de numeros.

    Paramnetro: lista_no_ordenada (str): Lista de números a ordenar.
    """
    # Retorna ordenada la lista recibida por parámetro
    lista_ordenada = sorted([int(x) for x in lista_no_ordenada.strip("[]").split(",")])
    # Retorna la hora actual formateada ("HHh:MM:SS")
    tiempo = datetime.now().strftime("%Hh:%M:%S")
    # Crea un formato JSON para la respuesta del Endpoint
    respuesta = {
                "hora_sistema": tiempo,
                "lista_ordenada": lista_ordenada,
            }
    return respuesta


@app.get("/healthcheck")
def get_health_check():
    """
    Endpoint para verificar el estado del API
    """
    return "OK"