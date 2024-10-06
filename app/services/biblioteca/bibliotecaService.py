from app.repositories.biblioteca import bibliotecaRepository

class BibliotecasService:
    def get_bibliotecas(self):
        bibliotecas = bibliotecaRepository.repo_get_bibliotecas()
        result = [
            {
                'biblioteca_id': biblioteca.id,
                'nombre_biblioteca': biblioteca.nombre_biblioteca,
                'direccion': biblioteca.direccion,
                'telefono': biblioteca.telefono,
                'email': biblioteca.email,
                'status': biblioteca.status,
                'created_at': biblioteca.created_at
            } for biblioteca in bibliotecas
        ]
        return result, 200

    def get_biblioteca(self, id):
        biblioteca = bibliotecaRepository.repo_get_biblioteca(id)
        if biblioteca:
            result = {
                'biblioteca_id': biblioteca.id,
                'nombre_biblioteca': biblioteca.nombre_biblioteca,
                'direccion': biblioteca.direccion,
                'telefono': biblioteca.telefono,
                'email': biblioteca.email,
                'status': biblioteca.status,
                'created_at': biblioteca.created_at
            }
            return result, 200
        return {'message': 'Biblioteca no encontrada'}, 404

# Instancia del servicio
bibliotecas_service = BibliotecasService()