from app.models.libros import Libro
from app import db


def repo_create_libro(data):
    nuevo_libro = Libro(
        titulo=data.get("titulo"),
        isbn=data.get("isbn"),
        fecha_publicacion=data.get("fecha_publicacion"),
        editorial_id=data.get("editorial_id"),
        categoria_id=data.get("categoria_id"),
        biblioteca_id=data.get("biblioteca_id"),
        status=data.get("status", True),
    )
    db.session.add(nuevo_libro)
    db.session.commit()
    return nuevo_libro


def repo_get_libros():
    return Libro.query.filter_by(status=True).all()


def repo_get_libro(id):
    try:
        libro = Libro.query.filter_by(libro_id=id, status=True).first()
        return libro
    except Exception as e:
        print(f"Error al obtener el libro con id {id}: {e}")
        return None


def repo_update_libro(id, data):
    try:
        libro = Libro.query.get(id)
        if libro:
            libro.titulo = data.get("titulo", libro.titulo)
            libro.isbn = data.get("isbn", libro.isbn)
            libro.fecha_publicacion = data.get(
                "fecha_publicacion", libro.fecha_publicacion
            )
            libro.editorial_id = data.get("editorial_id", libro.editorial_id)
            libro.categoria_id = data.get("categoria_id", libro.categoria_id)
            libro.biblioteca_id = data.get("biblioteca_id", libro.biblioteca_id)
            libro.status = data.get("status", libro.status)
            db.session.commit()
        return libro
    except Exception as e:
        print(f"Error al actualizar el libro con id {id}: {e}")
        return None


def repo_delete_libro(id):
    try:
        libro = Libro.query.get(id)
        if libro:
            libro.status = False
            db.session.commit()
    except Exception as e:
        print(f"Error al actualizar el estado del libro con id {id}: {e}")
