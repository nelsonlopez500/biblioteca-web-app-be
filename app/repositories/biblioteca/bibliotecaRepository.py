from app.models.biblioteca import Biblioteca
from app import db

def repo_create_biblioteca(data):
    nueva_biblioteca = Biblioteca(
        nombre_biblioteca=data.get('nombre_biblioteca'),
        direccion=data.get('direccion'),
        telefono=data.get('telefono'),
        email=data.get('email'),
        status=data.get('status', True)
    )
    db.session.add(nueva_biblioteca)
    db.session.commit()
    return nueva_biblioteca

def repo_get_bibliotecas():
    return Biblioteca.query.filter_by(status=True).all()

def repo_get_biblioteca(id):
    try:
        biblioteca = Biblioteca.query.filter_by(id=id, status=True).first()
        return biblioteca
    except Exception as e:
        print(f"Error al obtener la biblioteca con id {id}: {e}")
        return None

def repo_update_biblioteca(id, data):
    try:
        biblioteca = Biblioteca.query.get(id)
        if biblioteca:
            biblioteca.nombre_biblioteca = data['nombre_biblioteca']
            biblioteca.direccion = data.get('direccion', biblioteca.direccion)
            biblioteca.telefono = data.get('telefono', biblioteca.telefono)
            biblioteca.email = data.get('email', biblioteca.email)
            biblioteca.status = data.get('status', biblioteca.status)
            db.session.commit()
        return biblioteca
    except Exception as e:
        print(f"Error al actualizar la biblioteca con id {id}: {e}")
        return None

def repo_delete_biblioteca(id):
    try:
        biblioteca = Biblioteca.query.get(id)
        if biblioteca:
            biblioteca.status = False
            db.session.commit()
    except Exception as e:
        print(f"Error al actualizar el estado de la biblioteca con id {id}: {e}")