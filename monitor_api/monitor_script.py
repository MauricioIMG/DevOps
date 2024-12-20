import os
import time
import logging
import requests
from datetime import datetime

# Configuración del logging
logging.basicConfig(
    filename='/opt/monitor/logs/api-monitor.log',
    level=logging.INFO,
    format='%(message)s',
)

# Leer las variables de entorno
TARGET_CONTAINER_HOST = os.getenv('TARGET_CONTAINER_HOST', 'localhost')
TARGET_CONTAINER_PORT = os.getenv('TARGET_CONTAINER_PORT', '8001')
CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', 5))
URL = f"http://{TARGET_CONTAINER_HOST}:{TARGET_CONTAINER_PORT}/healthcheck"


def check_health():
    """Realiza una solicitud al endpoint /healthcheck y verifica la respuesta."""
    try:
        response = requests.get(URL)

        # Obtener fecha y hora actual
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if response.status_code == 200 and response.text == "OK":
            logging.info(f"{current_time} - INFO - API está operativa. Respuesta: {response.text}")
        else:
            logging.error(
                f"{current_time} - ERROR - API no responde correctamente. Estado: {response.status_code}, Respuesta: {response.text}")

    except requests.exceptions.RequestException as e:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.error(f"{current_time} - ERROR - Error al realizar la solicitud: {e}")


def main():
    """Función principal que inicia el monitoreo en un ciclo infinito."""
    while True:
        check_health()
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
