import os
from dotenv import load_dotenv
import urllib.parse

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Config:
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = urllib.parse.quote_plus(os.getenv('DB_PASSWORD'))
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        "?driver=ODBC+Driver+17+for+SQL+Server&timeout=30"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
