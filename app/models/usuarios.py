from app import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'  # Nombre de la tabla en la base de datos
    id = db.Column('usuario_id', db.Integer, primary_key=True, autoincrement=True)  # Campo id autoincremental
    nombre = db.Column(db.String(100), nullable=False)  # Nombre del usuario
    apellido = db.Column(db.String(100), nullable=False)  # Apellido del usuario
    direccion = db.Column(db.String(255), nullable=True)  # Dirección del usuario
    telefono = db.Column(db.String(20), nullable=True)  # Teléfono del usuario
    email = db.Column(db.String(100), nullable=True)  # Email del usuario
    fecha_registro = db.Column(db.Date, nullable=False)  # Fecha de registro del usuario
    rol_id = db.Column(db.Integer, nullable=True)  # ID del rol del usuario
    biblioteca_id = db.Column(db.Integer, nullable=True)  # ID de la biblioteca del usuario
    status = db.Column(db.Boolean, nullable=True)  # Estado del usuario
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Fecha de creación del registro

    def __repr__(self):
        return f'<Usuario {self.nombre} {self.apellido}>'
