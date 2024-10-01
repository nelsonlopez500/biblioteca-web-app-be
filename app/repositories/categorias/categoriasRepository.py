from app import db
from models import Categoria


def create_categoria(data):
    nueva_categoria = Categoria(
        nombre_categoria=data['nombre_categoria'],
        status=data.get('status', True),
        created_at=data.get('created_at')
    )
    db.session.add(nueva_categoria)
    db.session.commit()
    return nueva_categoria

def get_categorias():
    return Categoria.query.all()

def get_categoria(id):
    return Categoria.query.get_or_404(id)

def update_categoria(categoria, data):
    categoria.nombre_categoria = data['nombre_categoria']
    categoria.status = data.get('status', categoria.status)
    categoria.created_at = data.get('created_at', categoria.created_at)
    db.session.commit()
    return categoria

def delete_categoria(categoria):
    db.session.delete(categoria)
    db.session.commit()
