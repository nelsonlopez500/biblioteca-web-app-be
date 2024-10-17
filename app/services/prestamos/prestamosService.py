from app.repositories.prestamos import prestamosRepository


class PrestamosService:
    def create_prestamo(self, data):
        nuevo_prestamo = prestamosRepository.repo_create_prestamo(data)
        return {"message": "Préstamo creado exitosamente"}, 201

    def get_prestamos(self):
        prestamos = prestamosRepository.repo_get_prestamos()
        result = [
            {
                "prestamo_id": prestamo.prestamo_id,
                "usuario_id": prestamo.usuario_id,
                "libro_id": prestamo.libro_id,
                "fecha_prestamo": prestamo.fecha_prestamo,
                "fecha_vencimiento": prestamo.fecha_vencimiento,
                "estado_prestamo": prestamo.estado_prestamo,
                "biblioteca_id": prestamo.biblioteca_id,
                "created_at": prestamo.created_at,
            }
            for prestamo in prestamos
        ]
        return result, 200

    def get_prestamo(self, id):
        prestamo = prestamosRepository.repo_get_prestamo(id)
        if prestamo:
            result = {
                "prestamo_id": prestamo.prestamo_id,
                "usuario_id": prestamo.usuario_id,
                "libro_id": prestamo.libro_id,
                "fecha_prestamo": prestamo.fecha_prestamo,
                "fecha_vencimiento": prestamo.fecha_vencimiento,
                "estado_prestamo": prestamo.estado_prestamo,
                "biblioteca_id": prestamo.biblioteca_id,
                "created_at": prestamo.created_at,
            }
            return result, 200
        return {
            "message": "Préstamo no encontrado"
        }, 404  # Manejo de error si no se encuentra

    def update_prestamo(self, id, data):
        prestamo = prestamosRepository.repo_get_prestamo(id)
        if not prestamo:
            return {
                "message": "Préstamo no encontrado"
            }, 404  # Manejo de error si no se encuentra

        prestamosRepository.repo_update_prestamo(id, data)
        return {"message": "Préstamo actualizado exitosamente"}, 200

    def delete_prestamo(self, id):
        prestamo = prestamosRepository.repo_get_prestamo(id)
        if not prestamo:
            return {
                "message": "Préstamo no encontrado"
            }, 404  # Manejo de error si no se encuentra

        prestamosRepository.repo_delete_prestamo(id)
        return {"message": "Préstamo eliminado exitosamente"}, 200


# Instancia del servicio
prestamos_service = PrestamosService()