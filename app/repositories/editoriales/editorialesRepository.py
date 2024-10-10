from app.models.editoriales import Editorial
from app import db


def repo_create_editorial(data):
    nueva_editorial = Editorial(
        nombre_editorial=data.get("nombre_editorial"), status=data.get("status", True)
    )
    db.session.add(nueva_editorial)
    db.session.commit()
    return nueva_editorial


def repo_get_editoriales():
    return Editorial.query.filter_by(status=True).all()


def repo_get_editorial(id):
    try:
        editorial = Editorial.query.filter_by(id=id, status=True).first()
        return editorial
    except Exception as e:
        print(f"Error al obtener la editorial con id {id}: {e}")
        return None


def repo_update_editorial(id, data):
    try:
        editorial = Editorial.query.get(id)
        if editorial:
            editorial.nombre_editorial = data["nombre_editorial"]
            editorial.status = data.get("status", editorial.status)
            db.session.commit()
        return editorial
    except Exception as e:
        print(f"Error al actualizar la editorial con id {id}: {e}")
        return None


def repo_delete_editorial(id):
    try:
        editorial = Editorial.query.get(id)
        if editorial:
            editorial.status = (
                False
            )
            db.session.commit()
    except Exception as e:
        print(f"Error al actualizar el estado de la editorial con id {id}: {e}")
