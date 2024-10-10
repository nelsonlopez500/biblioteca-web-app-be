from app.repositories.libros import librosRepository


class LibrosService:
    def create_libro(self, data):
        nuevo_libro = librosRepository.repo_create_libro(data)
        return {"message": "Libro creado exitosamente"}, 201

    def get_libros(self):
        libros = librosRepository.repo_get_libros()
        result = [
            {
                "libro_id": libro.libro_id,
                "titulo": libro.titulo,
                "isbn": libro.isbn,
                "fecha_publicacion": libro.fecha_publicacion,
                "editorial_id": libro.editorial_id,
                "categoria_id": libro.categoria_id,
                "biblioteca_id": libro.biblioteca_id,
                "status": libro.status,
                "created_at": libro.created_at,
            }
            for libro in libros
        ]
        return result, 200

    def get_libro(self, id):
        libro = librosRepository.repo_get_libro(id)
        if libro:
            result = {
                "libro_id": libro.libro_id,
                "titulo": libro.titulo,
                "isbn": libro.isbn,
                "fecha_publicacion": libro.fecha_publicacion,
                "editorial_id": libro.editorial_id,
                "categoria_id": libro.categoria_id,
                "biblioteca_id": libro.biblioteca_id,
                "status": libro.status,
                "created_at": libro.created_at,
            }
            return result, 200
        return {
            "message": "Libro no encontrado"
        }, 404  # Manejo de error si no se encuentra

    def update_libro(self, id, data):
        libro = librosRepository.repo_get_libro(id)
        if not libro:
            return {
                "message": "Libro no encontrado"
            }, 404  # Manejo de error si no se encuentra

        librosRepository.repo_update_libro(id, data)
        return {"message": "Libro actualizado exitosamente"}, 200

    def delete_libro(self, id):
        libro = librosRepository.repo_get_libro(id)
        if not libro:
            return {
                "message": "Libro no encontrado"
            }, 404  # Manejo de error si no se encuentra

        librosRepository.repo_delete_libro(id)
        return {"message": "Libro eliminado exitosamente"}, 200


# Instancia del servicio
libros_service = LibrosService()
