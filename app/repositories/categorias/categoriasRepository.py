from sqlobject.sqlbuilder import Insert, Select, AND
from datetime import datetime
from app.models.categorias import Categoria  # Importa el modelo Categoria

def repo_create_categoria(data):
    nueva_categoria = Categoria(
        nombre_categoria=data.get('nombre_categoria'),
        status=data.get('status', True)
    )
    nueva_categoria.flush() 
    return nueva_categoria

def repo_get_categorias():
    return list(Categoria.select())

def repo_get_categoria(id):
    try:
        return Categoria.get(id)
    except Exception as e:
        # Manejo de errores, tal vez lanzar una excepción personalizada
        print(f"Error al obtener la categoría con id {id}: {e}")
        return None

def repo_update_categoria(id, data):
    try:
        categoria = Categoria.get(id)
        categoria.set(
            nombre_categoria=data['nombre_categoria'],
            status=data.get('status', categoria.status)  # Mantener el valor existente si no se proporciona uno nuevo
            # No actualizamos created_at
        )
        return categoria
    except Exception as e:
        # Manejo de errores
        print(f"Error al actualizar la categoría con id {id}: {e}")
        return None

def repo_delete_categoria(id):
    try:
        categoria = Categoria.get(id)
        categoria.destroySelf()
    except Exception as e:
        # Manejo de errores
        print(f"Error al eliminar la categoría con id {id}: {e}")
