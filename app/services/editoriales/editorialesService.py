from app.repositories.editoriales import editorialesRepository

class EditorialesService:
    def create_editorial(self, data):
        nueva_editorial = editorialesRepository.repo_create_editorial(data)
        return {'message': 'Editorial creada exitosamente'}, 201

    def get_editoriales(self):
        editoriales = editorialesRepository.repo_get_editoriales()
        result = [
            {
                'editorial_id': editorial.id,
                'nombre_editorial': editorial.nombre_editorial,
                'status': editorial.status,
                'created_at': editorial.created_at
            } for editorial in editoriales
        ]
        return result, 200

    def get_editorial(self, id):
        editorial = editorialesRepository.repo_get_editorial(id)
        if editorial:
            result = {
                'editorial_id': editorial.id,
                'nombre_editorial': editorial.nombre_editorial,
                'status': editorial.status,
                'created_at': editorial.created_at
            }
            return result, 200
        return {'message': 'Editorial no encontrada'}, 404  # Manejo de error si no se encuentra

    def update_editorial(self, id, data):
        editorial = editorialesRepository.repo_get_editorial(id)
        if not editorial:
            return {'message': 'Editorial no encontrada'}, 404  # Manejo de error si no se encuentra
        
        editorialesRepository.repo_update_editorial(id, data)
        return {'message': 'Editorial actualizada exitosamente'}, 200

    def delete_editorial(self, id):
        editorial = editorialesRepository.repo_get_editorial(id)
        if not editorial:
            return {'message': 'Editorial no encontrada'}, 404  # Manejo de error si no se encuentra

        editorialesRepository.repo_delete_editorial(id)
        return {'message': 'Editorial eliminada exitosamente'}, 200

# Instancia del servicio
editoriales_service = EditorialesService()
