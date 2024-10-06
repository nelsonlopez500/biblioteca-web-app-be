from app import db
from datetime import datetime

class Categoria(db.Model):
    __tablename__ = 'categorias'  # Nombre de la tabla en la base de datos
    id = db.Column('categoria_id', db.Integer, primary_key=True)  # Campo id autoincremental
    nombre_categoria = db.Column(db.String(100), unique=True, nullable=False)  # Nombre de la categoría
    status = db.Column(db.Boolean, default=True)  # Estado de la categoría
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Fecha de creación

    def __repr__(self):
        return f'<Categoria {self.nombre_categoria}>'