from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/lista-ordenada")
async def get_ordered_list(lista_no_ordenada: str):
    ordered_list = sorted([x for x in lista_no_ordenada if x.isdigit()])
    tiempo = datetime.now().strftime("%Hh:%M:%S")
    return {
                "system_time": tiempo,
                "ordered_list": ordered_list,
            }

@app.get("/healthcheck")
def get_health_check():
    return "Ok"