from flask import Flask, redirect
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()  # Crear una única instancia de SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar SQLAlchemy con la aplicación
    db.init_app(app)

    # Inicializar Swagger
    swagger = Swagger(app)

    # Ruta raíz para redirigir a la documentación de Swagger
    @app.route('/')
    def index():
        return redirect('/apidocs')

    # Registrar los blueprints
    from app.controllers.categorias.categoriasController import categorias_bp
    app.register_blueprint(categorias_bp, url_prefix='/api')

    # Crear las tablas en la base de datos
    with app.app_context():
        db.create_all()

    return app
