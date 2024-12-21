"""Script con métodos de la aplicación monitoreo-api"""

# External libraries
import os
import time
import logging
import requests


logging.basicConfig(
    filename='/opt/monitor/logs/api-monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S,%f'
)

TARGET_CONTAINER_HOST = os.getenv('TARGET_CONTAINER_HOST', 'localhost')
TARGET_CONTAINER_PORT = os.getenv('TARGET_CONTAINER_PORT', '8001')
CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', 5))
URL = f"http://{TARGET_CONTAINER_HOST}:{TARGET_CONTAINER_PORT}/healthcheck"


def check_health():
    """Realiza una solicitud al endpoint /healthcheck y verifica la respuesta."""
    try:
        response = requests.get(URL)
        respuesta = response.text
        if response.status_code == 200 and respuesta == '"OK"':
            logging.info(
                f"Se hizo la solicitud al endpoint {URL} y devolvió OK")
        else:
            logging.error(
                f"Se hizo la solicitud al endpoint {URL} y devolvió error: "
                f"Código de estado: {response.status_code}, Respuesta: {response.text}"
            )

    except requests.exceptions.RequestException as e:
        logging.error(
            f"Se hizo la solicitud al endpoint {URL} y devolvió error: {e}")


def main():
    """Función principal que inicia el monitoreo en un ciclo infinito."""
    while True:
        check_health()
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()

