from app.repositories.categorias import categoriasRepository

class CategoriasService:
    def create_categoria(self, data):
        nueva_categoria = categoriasRepository.repo_create_categoria(data)
        return {'message': 'Categoría creada exitosamente'}, 201

    def get_categorias(self):
        categorias = categoriasRepository.repo_get_categorias()
        result = [
            {
                'categoria_id': categoria.id,  # Cambiado de categoria.categoria_id a categoria.id
                'nombre_categoria': categoria.nombre_categoria,
                'status': categoria.status,
                'created_at': categoria.created_at
            } for categoria in categorias
        ]
        return result, 200

    def get_categoria(self, id):
        categoria = categoriasRepository.repo_get_categoria(id)
        if categoria:
            result = {
                'categoria_id': categoria.id,  # Cambiado de categoria.categoria_id a categoria.id
                'nombre_categoria': categoria.nombre_categoria,
                'status': categoria.status,
                'created_at': categoria.created_at
            }
            return result, 200
        return {'message': 'Categoría no encontrada'}, 404  # Manejo de error si no se encuentra

    def update_categoria(self, id, data):
        categoria = categoriasRepository.repo_get_categoria(id)
        if not categoria:
            return {'message': 'Categoría no encontrada'}, 404  # Manejo de error si no se encuentra
        
        categoriasRepository.repo_update_categoria(id, data)  # Asegúrate de pasar el id aquí
        return {'message': 'Categoría actualizada exitosamente'}, 200

    def delete_categoria(self, id):
        categoria = categoriasRepository.repo_get_categoria(id)
        if not categoria:
            return {'message': 'Categoría no encontrada'}, 404  # Manejo de error si no se encuentra

        categoriasRepository.repo_delete_categoria(id)  # Cambiado para pasar solo el id
        return {'message': 'Categoría eliminada exitosamente'}, 200

# Instancia del servicio
categorias_service = CategoriasService()
