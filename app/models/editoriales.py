from app import db
from datetime import datetime

class Editorial(db.Model):
    __tablename__ = 'editoriales'  # Nombre de la tabla en la base de datos
    id = db.Column('editorial_id', db.Integer, primary_key=True)  # Campo id autoincremental
    nombre_editorial = db.Column(db.String(255), nullable=False)  # Nombre de la editorial
    status = db.Column(db.Boolean, default=True)  # Estado de la editorial
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Fecha de creación

    def __repr__(self):
        return f'<Editorial {self.nombre_editorial}>'
