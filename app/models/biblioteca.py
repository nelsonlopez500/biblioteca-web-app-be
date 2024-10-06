from app import db
from datetime import datetime

class Biblioteca(db.Model):
    __tablename__ = 'bibliotecas'  # Nombre de la tabla en la base de datos
    id = db.Column('biblioteca_id', db.Integer, primary_key=True)  # Campo id autoincremental
    nombre_biblioteca = db.Column(db.String(255), nullable=False)  # Nombre de la biblioteca
    direccion = db.Column(db.String(255), nullable=True)  # Dirección de la biblioteca
    telefono = db.Column(db.String(20), nullable=True)  # Teléfono de la biblioteca
    email = db.Column(db.String(100), nullable=True)  # Email de la biblioteca
    status = db.Column(db.Boolean, default=True)  # Estado de la biblioteca
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Fecha de creación

    def __repr__(self):
        return f'<Biblioteca {self.nombre_biblioteca}>'