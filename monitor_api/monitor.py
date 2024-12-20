import os
import time
import requests
from datetime import datetime

# Obtiene las variables de entorno
TARGET_CONTAINER_HOST = os.getenv('TARGET_CONTAINER_HOST', 'localhost')
TARGET_CONTAINER_PORT = os.getenv('TARGET_CONTAINER_PORT', '8001')
CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', 5))
LOG_FILE_PATH = "/opt/monitor/logs/api-monitor.log"

# URL del endpoint healthcheck
url = f"http://{TARGET_CONTAINER_HOST}:{TARGET_CONTAINER_PORT}/healthcheck"

# Función para registrar los logs
def log_health_check(status):
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(f"{datetime.now()} - {status}\n")

# Monitoreo continuo
while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            log_health_check("OK")
        else:
            log_health_check(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        log_health_check(f"Exception: {e}")

    time.sleep(CHECK_INTERVAL)
