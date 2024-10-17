from app.models.usuarios import Usuario
from app import db
from datetime import datetime

def repo_create_usuario(data):
    nuevo_usuario = Usuario(
        nombre=data.get('nombre'),
        apellido=data.get('apellido'),
        direccion=data.get('direccion'),
        telefono=data.get('telefono'),
        email=data.get('email'),
        fecha_registro=data.get('fecha_registro', datetime.utcnow().date()),  # Usa la fecha actual si no se proporciona
        rol_id=data.get('rol_id'),
        biblioteca_id=data.get('biblioteca_id'),
        status=data.get('status', True),  # Valor por defecto True si no se especifica
        created_at=datetime.utcnow()
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return nuevo_usuario

def repo_get_usuarios():
    return Usuario.query.filter_by(status=True).all()

def repo_get_usuario(id):
    try:
        usuario = Usuario.query.filter_by(id=id, status=True).first()
        return usuario
    except Exception as e:
        print(f"Error al obtener el usuario con id {id}: {e}")
        return None

def repo_update_usuario(id, data):
    try:
        usuario = Usuario.query.get(id)
        if usuario:
            usuario.nombre = data.get('nombre', usuario.nombre)
            usuario.apellido = data.get('apellido', usuario.apellido)
            usuario.direccion = data.get('direccion', usuario.direccion)
            usuario.telefono = data.get('telefono', usuario.telefono)
            usuario.email = data.get('email', usuario.email)
            usuario.rol_id = data.get('rol_id', usuario.rol_id)
            usuario.biblioteca_id = data.get('biblioteca_id', usuario.biblioteca_id)
            usuario.status = data.get('status', usuario.status)
            db.session.commit()
        return usuario
    except Exception as e:
        print(f"Error al actualizar el usuario con id {id}: {e}")
        return None

def repo_delete_usuario(id):
    try:
        usuario = Usuario.query.get(id)
        if usuario:
            usuario.status = False  # Cambia el estado en lugar de eliminarlo físicamente
            db.session.commit()
    except Exception as e:
        print(f"Error al actualizar el estado del usuario con id {id}: {e}")
