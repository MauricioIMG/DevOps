# librerías externas
import os
from functools import lru_cache
from pymongo import MongoClient
from pymongo.database import Database


def create_mongo_client() -> MongoClient:
    """Crea y devuelve un cliente de MongoDB usando las variables de entorno."""
    # Usa un valor por defecto si no está definido
    mongo_host = os.environ.get('MONGODB_HOST', 'localhost')
    # Convierte el puerto a entero
    mongo_port = int(os.environ.get('MONGODB_PORT', 27017))

    return MongoClient(host=mongo_host, port=mongo_port)


@lru_cache()
def get_mongo_db() -> Database:
    """Devuelve la base de datos 'python_app' desde el cliente MongoDB.

    Returns:
        La base de datos 'python_app'.
    """
    # Usa la función auxiliar para crear el cliente
    client = create_mongo_client()
    # Accede a la base de datos 'python_app'
    mongo_db = client.python_app

    return mongo_db
