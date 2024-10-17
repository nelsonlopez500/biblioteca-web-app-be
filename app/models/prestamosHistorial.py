from app import db
from datetime import datetime

class PrestamosHistorial(db.Model):
    __tablename__ = 'prestamos_historial'  # Table name in the database

    historial_id = db.Column(db.Integer, primary_key=True)  # Primary key, IDENTITY field
    prestamo_id = db.Column(db.Integer, db.ForeignKey('prestamos.prestamo_id'), nullable=False)  # Foreign key to the prestamos table
    fecha_accion = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Action date, mandatory field
    accion = db.Column(db.String(100), nullable=False)  # Action description, mandatory field
    descripcion = db.Column(db.Text)  # Description (can be null)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Creation date, default to current date

    def __repr__(self):
        return f'<Historial ID: {self.historial_id} - Prestamo ID: {self.prestamo_id} - Accion: {self.accion}>'
