from app import db
from datetime import datetime

class Libro(db.Model):
    __tablename__ = 'libros'  # Nombre de la tabla en la base de datos

    libro_id = db.Column(db.Integer, primary_key=True)  # Clave primaria, campo IDENTITY
    titulo = db.Column(db.String(255), nullable=False)  # Campo título obligatorio
    isbn = db.Column(db.String(20), nullable=False, unique=True)  # Campo ISBN único y obligatorio
    fecha_publicacion = db.Column(db.Date)  # Campo fecha de publicación (puede ser nulo)
    editorial_id = db.Column(db.Integer)  # Clave foránea hacia la tabla editoriales
    categoria_id = db.Column(db.Integer)  # Clave foránea hacia la tabla categorías
    biblioteca_id = db.Column(db.Integer)  # Clave foránea hacia la tabla bibliotecas
    status = db.Column(db.Boolean, default=True)  # Campo de estado, con valor predeterminado True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Campo de fecha de creación, valor predeterminado la fecha actual

    def __repr__(self):
        return f'<Libro {self.titulo} - ISBN: {self.isbn}>'
