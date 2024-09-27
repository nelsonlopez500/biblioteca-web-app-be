from flask import Flask, redirect
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializar SQLAlchemy
    db.init_app(app)

    # Inicializar Swagger
    swagger = Swagger(app)

    # Ruta raíz para redirigir a la documentación de Swagger
    @app.route('/')
    def index():
        return redirect('/apidocs')

    # Registrar el blueprint de ejemplos
    from .controllers.ejemplos.ejemplos import ejemplos_bp
    app.register_blueprint(ejemplos_bp, url_prefix='/api')

    return app