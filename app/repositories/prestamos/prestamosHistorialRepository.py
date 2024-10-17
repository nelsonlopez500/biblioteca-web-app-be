from app.models.prestamosHistorial import PrestamosHistorial
from app import db


def repo_create_prestamo_historial(data):
    nuevo_historial = PrestamosHistorial(
        prestamo_id=data.get("prestamo_id"),
        fecha_accion=data.get("fecha_accion"),
        accion=data.get("accion"),
        descripcion=data.get("descripcion"),
    )
    db.session.add(nuevo_historial)
    db.session.commit()
    return nuevo_historial


def repo_get_prestamos_historial():
    return PrestamosHistorial.query.all()


def repo_get_prestamo_historial(id):
    try:
        historial = PrestamosHistorial.query.filter_by(historial_id=id).first()
        return historial
    except Exception as e:
        print(f"Error al obtener el historial con id {id}: {e}")
        return None


def repo_update_prestamo_historial(id, data):
    try:
        historial = PrestamosHistorial.query.get(id)
        if historial:
            historial.prestamo_id = data.get("prestamo_id", historial.prestamo_id)
            historial.fecha_accion = data.get("fecha_accion", historial.fecha_accion)
            historial.accion = data.get("accion", historial.accion)
            historial.descripcion = data.get("descripcion", historial.descripcion)
            db.session.commit()
        return historial
    except Exception as e:
        print(f"Error al actualizar el historial con id {id}: {e}")
        return None


def repo_delete_prestamo_historial(id):
    try:
        historial = PrestamosHistorial.query.get(id)
        if historial:
            db.session.delete(historial)
            db.session.commit()
    except Exception as e:
        print(f"Error al eliminar el historial con id {id}: {e}")
