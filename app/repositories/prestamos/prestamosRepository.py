from app.models.prestamos import Prestamo
from app import db


def repo_create_prestamo(data):
    nuevo_prestamo = Prestamo(
        usuario_id=data.get("usuario_id"),
        libro_id=data.get("libro_id"),
        fecha_prestamo=data.get("fecha_prestamo"),
        fecha_vencimiento=data.get("fecha_vencimiento"),
        estado_prestamo=data.get("estado_prestamo"),
        biblioteca_id=data.get("biblioteca_id"),
        created_at=data.get("created_at", None),  # Puedes establecer la fecha de creación manualmente si lo deseas
    )
    db.session.add(nuevo_prestamo)
    db.session.commit()
    return nuevo_prestamo


def repo_get_prestamos():
    return Prestamo.query.all()  # Puedes agregar filtros según tus necesidades


def repo_get_prestamo(id):
    try:
        prestamo = Prestamo.query.get(id)
        return prestamo
    except Exception as e:
        print(f"Error al obtener el préstamo con id {id}: {e}")
        return None


def repo_update_prestamo(id, data):
    try:
        prestamo = Prestamo.query.get(id)
        if prestamo:
            prestamo.usuario_id = data.get("usuario_id", prestamo.usuario_id)
            prestamo.libro_id = data.get("libro_id", prestamo.libro_id)
            prestamo.fecha_prestamo = data.get("fecha_prestamo", prestamo.fecha_prestamo)
            prestamo.fecha_vencimiento = data.get("fecha_vencimiento", prestamo.fecha_vencimiento)
            prestamo.estado_prestamo = data.get("estado_prestamo", prestamo.estado_prestamo)
            prestamo.biblioteca_id = data.get("biblioteca_id", prestamo.biblioteca_id)
            db.session.commit()
        return prestamo
    except Exception as e:
        print(f"Error al actualizar el préstamo con id {id}: {e}")
        return None


def repo_delete_prestamo(id):
    try:
        prestamo = Prestamo.query.get(id)
        if prestamo:
            db.session.delete(prestamo)  # Eliminar el préstamo directamente
            db.session.commit()
    except Exception as e:
        print(f"Error al eliminar el préstamo con id {id}: {e}")