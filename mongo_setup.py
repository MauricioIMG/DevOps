# librerías externas
import os
from functools import lru_cache
from pymongo import MongoClient
from pymongo.database import Database


def create_mongo_client() -> MongoClient:
    """Crea y devuelve un cliente de MongoDB usando las variables de entorno.
    """
    mongo_host = os.getenv('MONGODB_HOST', 'localhost')
    mongo_port = int(os.getenv('MONGODB_PORT', 27017))

    try:
        # Devuelve el cliente MongoDB con el host y puerto obtenidos
        client = MongoClient(host=mongo_host, port=mongo_port)
        return client
    except Exception as e:
        raise ConnectionError(f"Error al conectar con MongoDB: {e}")


@lru_cache()
def get_mongo_db() -> Database:
    """Devuelve la base de datos 'python_app' desde el cliente MongoDB.

    Returns:
        La base de datos 'python_app'.
    """
    # Usa la función auxiliar para crear el cliente de MongoDB
    client = create_mongo_client()

    try:
        # Accede a la base de datos 'python_app'
        mongo_db = client.python_app
        return mongo_db
    except Exception as e:
        raise ConnectionError(f"Error al acceder a la base de datos: {e}")
