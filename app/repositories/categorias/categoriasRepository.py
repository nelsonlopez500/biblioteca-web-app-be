from app.models.categorias import Categoria
from app import db

def repo_create_categoria(data):
    nueva_categoria = Categoria(
        nombre_categoria=data.get('nombre_categoria'),
        status=data.get('status', True)
    )
    db.session.add(nueva_categoria)
    db.session.commit()
    return nueva_categoria

def repo_get_categorias():
    return Categoria.query.filter_by(status=True).all()

def repo_get_categoria(id):
    try:
        categoria = Categoria.query.filter_by(id=id, status=True).first()
        return categoria
    except Exception as e:
        print(f"Error al obtener la categoría con id {id}: {e}")
        return None

def repo_update_categoria(id, data):
    try:
        categoria = Categoria.query.get(id)
        if categoria:
            categoria.nombre_categoria = data['nombre_categoria']
            categoria.status = data.get('status', categoria.status)
            db.session.commit()
        return categoria
    except Exception as e:
        print(f"Error al actualizar la categoría con id {id}: {e}")
        return None

def repo_delete_categoria(id):
    try:
        categoria = Categoria.query.get(id)
        if categoria:
            categoria.status = False
            db.session.commit()
    except Exception as e:
        print(f"Error al actualizar el estado de la categoría con id {id}: {e}")
