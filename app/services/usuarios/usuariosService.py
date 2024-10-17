from app.repositories.usuarios import usuariosRepository

class UsuariosService:
    def create_usuario(self, data):
        nuevo_usuario = usuariosRepository.repo_create_usuario(data)
        return {'message': 'Usuario creado exitosamente'}, 201

    def get_usuarios(self):
        usuarios = usuariosRepository.repo_get_usuarios()
        result = [
            {
                'usuario_id': usuario.id,  # Cambiado de usuario.usuario_id a usuario.id
                'nombre': usuario.nombre,
                'apellido': usuario.apellido,
                'direccion': usuario.direccion,
                'telefono': usuario.telefono,
                'email': usuario.email,
                'fecha_registro': usuario.fecha_registro,
                'rol_id': usuario.rol_id,
                'biblioteca_id': usuario.biblioteca_id,
                'status': usuario.status,
                'created_at': usuario.created_at
            } for usuario in usuarios
        ]
        return result, 200

    def get_usuario(self, id):
        usuario = usuariosRepository.repo_get_usuario(id)
        if usuario:
            result = {
                'usuario_id': usuario.id,  # Cambiado de usuario.usuario_id a usuario.id
                'nombre': usuario.nombre,
                'apellido': usuario.apellido,
                'direccion': usuario.direccion,
                'telefono': usuario.telefono,
                'email': usuario.email,
                'fecha_registro': usuario.fecha_registro,
                'rol_id': usuario.rol_id,
                'biblioteca_id': usuario.biblioteca_id,
                'status': usuario.status,
                'created_at': usuario.created_at
            }
            return result, 200
        return {'message': 'Usuario no encontrado'}, 404  # Manejo de error si no se encuentra

    def update_usuario(self, id, data):
        usuario = usuariosRepository.repo_get_usuario(id)
        if not usuario:
            return {'message': 'Usuario no encontrado'}, 404  # Manejo de error si no se encuentra
        
        usuariosRepository.repo_update_usuario(id, data)  # Asegúrate de pasar el id aquí
        return {'message': 'Usuario actualizado exitosamente'}, 200

    def delete_usuario(self, id):
        usuario = usuariosRepository.repo_get_usuario(id)
        if not usuario:
            return {'message': 'Usuario no encontrado'}, 404  # Manejo de error si no se encuentra

        usuariosRepository.repo_delete_usuario(id)  # Cambiado para pasar solo el id
        return {'message': 'Usuario eliminado exitosamente'}, 200

# Instancia del servicio
usuarios_service = UsuariosService()
