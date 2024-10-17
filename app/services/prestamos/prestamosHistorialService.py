from app.repositories.prestamos import prestamosHistorialRepository

class PrestamosHistorialService:

    def get_prestamos_historial(self):
        historiales = prestamosHistorialRepository.repo_get_prestamos_historial()
        result = [
            {
                "historial_id": historial.historial_id,
                "prestamo_id": historial.prestamo_id,
                "fecha_accion": historial.fecha_accion,
                "accion": historial.accion,
                "descripcion": historial.descripcion,
            }
            for historial in historiales
        ]
        return result, 200

    def get_prestamo_historial(self, id):
        historial = prestamosHistorialRepository.repo_get_prestamo_historial(id)
        if historial:
            result = {
                "historial_id": historial.historial_id,
                "prestamo_id": historial.prestamo_id,
                "fecha_accion": historial.fecha_accion,
                "accion": historial.accion,
                "descripcion": historial.descripcion,
            }
            return result, 200
        return {"message": "Historial de préstamo no encontrado"}, 404

# Instancia del servicio
prestamos_historial_service = PrestamosHistorialService()
