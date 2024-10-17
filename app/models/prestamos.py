from app import db
from datetime import datetime

class Prestamo(db.Model):
    __tablename__ = 'prestamos'  # Nombre de la tabla en la base de datos

    prestamo_id = db.Column(db.Integer, primary_key=True)  # Clave primaria, campo IDENTITY
    usuario_id = db.Column(db.Integer, nullable=False)  # Clave foránea hacia la tabla de usuarios
    libro_id = db.Column(db.Integer, nullable=False)  # Clave foránea hacia la tabla de libros
    fecha_prestamo = db.Column(db.DateTime, nullable=False)  # Fecha de préstamo, campo obligatorio
    fecha_vencimiento = db.Column(db.DateTime)  # Fecha de vencimiento (puede ser nulo)
    estado_prestamo = db.Column(db.String(255))  # Estado del préstamo (puede ser nulo)
    biblioteca_id = db.Column(db.Integer, nullable=False)  # Clave foránea hacia la tabla de bibliotecas
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Fecha de creación, valor predeterminado la fecha actual

    def __repr__(self):
        return f'<Prestamo ID: {self.prestamo_id} - Usuario ID: {self.usuario_id} - Libro ID: {self.libro_id}>'