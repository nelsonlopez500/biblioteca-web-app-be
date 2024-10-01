from repositories.categorias import categoriasRepository

class CategoriasService:
    def create_categoria(self, data):
        nueva_categoria = categoriasRepository.repo_create_categoria(data)
        return {'message': 'Categoría creada exitosamente'}, 201

    def get_categorias(self):
        categorias = categoriasRepository.repo_get_categorias()
        result = [
            {
                'categoria_id': categoria.categoria_id,
                'nombre_categoria': categoria.nombre_categoria,
                'status': categoria.status,
                'created_at': categoria.created_at
            } for categoria in categorias
        ]
        return result, 200

    def get_categoria(self, id):
        categoria = categoriasRepository.repo_get_categoria(id)
        result = {
            'categoria_id': categoria.categoria_id,
            'nombre_categoria': categoria.nombre_categoria,
            'status': categoria.status,
            'created_at': categoria.created_at
        }
        return result, 200

    def update_categoria(self, id, data):
        categoria = categoriasRepository.repo_get_categoria(id)
        updated_categoria = categoriasRepository.repo_update_categoria(
            categoria, data)
        return {'message': 'Categoría actualizada exitosamente'}, 200

    def delete_categoria(self, id):
        categoria = categoriasRepository.repo_get_categoria(id)
        categoriasRepository.repo_delete_categoria(categoria)
        return {'message': 'Categoría eliminada exitosamente'}, 200


# Instancia del servicio
categorias_service = CategoriasService()
