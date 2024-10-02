from sqlobject.sqlbuilder import Insert, Select, AND
from datetime import datetime
from app.models.categorias import Categoria  # Importa el modelo Categoria

def repo_create_categoria(data):
    nueva_categoria = Categoria(
        nombre_categoria=data['nombre_categoria'],
        status=data.get('status', True),
        created_at=data.get('created_at', datetime.now())
    )
    return nueva_categoria

def repo_get_categorias():
    return list(Categoria.select())

def repo_get_categoria(id):
    return Categoria.get(id)

def repo_update_categoria(id, data):
    categoria = Categoria.get(id)
    categoria.set(
        nombre_categoria=data['nombre_categoria'],
        status=data.get('status', True),
        created_at=data.get('created_at', datetime.now())
    )
    return categoria

def repo_delete_categoria(id):
    categoria = Categoria.get(id)
    categoria.destroySelf()