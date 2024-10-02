from flask import Flask, redirect
from flasgger import Swagger
from sqlobject import sqlhub, connectionForURI

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Establecer la conexión a la base de datos
    connection_string = app.config['DATABASE_URI']
    conn = connectionForURI(connection_string)
    sqlhub.processConnection = conn

    # Inicializar Swagger
    swagger = Swagger(app)

    # Ruta raíz para redirigir a la documentación de Swagger
    @app.route('/')
    def index():
        return redirect('/apidocs')

    # Registrar el blueprint de ejemplos
    from app.controllers.ejemplos.ejemplos import ejemplos_bp
    app.register_blueprint(ejemplos_bp, url_prefix='/api')

    # Registrar el blueprint de categorías
    from app.controllers.categorias.categoriasController import categorias_bp
    app.register_blueprint(categorias_bp, url_prefix='/api')

    return app