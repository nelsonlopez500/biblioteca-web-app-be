import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Config:
    DATABASE_URI = os.getenv('DATABASE_URI')