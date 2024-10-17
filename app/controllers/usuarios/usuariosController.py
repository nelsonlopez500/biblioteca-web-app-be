from flask import Blueprint, request, jsonify
from app.services.usuarios.usuariosService import usuarios_service

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['POST'])
def create_usuario_route():
    """
    Crear un nuevo usuario
    ---
    tags:
      - usuarios
    parameters:
      - in: body
        name: body
        required: True
        schema:
          id: Usuario
          required:
            - nombre
            - apellido
            - email
          properties:
            nombre:
              type: string
              example: "Juan"
            apellido:
              type: string
              example: "Perez"
            email:
              type: string
              example: "juan.perez@example.com"
            telefono:
              type: string
              example: "555-1234"
            direccion:
              type: string
              example: "123 Calle Falsa"
    responses:
      201:
        description: Usuario creado exitosamente
        examples:
          application/json: {"usuario_id": 1, "nombre": "Juan", "apellido": "Perez"}
    """
    data = request.get_json()
    response, status = usuarios_service.create_usuario(data)
    return jsonify(response), status

@usuarios_bp.route('/usuarios', methods=['GET'])
def get_usuarios_route():
    """
    Obtener todos los usuarios
    ---
    tags:
      - usuarios
    responses:
      200:
        description: Lista de todos los usuarios
        examples:
          application/json: [
            {"usuario_id": 1, "nombre": "Juan", "apellido": "Perez"},
            {"usuario_id": 2, "nombre": "Maria", "apellido": "Gomez"}
          ]
    """
    response, status = usuarios_service.get_usuarios()
    return jsonify(response), status

@usuarios_bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario_route(id):
    """
    Obtener un usuario por ID
    ---
    tags:
      - usuarios
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del usuario
    responses:
      200:
        description: Usuario obtenido exitosamente
        examples:
          application/json: {"usuario_id": 1, "nombre": "Juan", "apellido": "Perez"}
      404:
        description: Usuario no encontrado
        examples:
          application/json: {"error": "Usuario no encontrado"}
    """
    response, status = usuarios_service.get_usuario(id)
    return jsonify(response), status

@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario_route(id):
    """
    Actualizar un usuario existente
    ---
    tags:
      - usuarios
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del usuario
      - in: body
        name: body
        required: True
        schema:
          id: Usuario
          required:
            - nombre
            - apellido
            - email
          properties:
            nombre:
              type: string
              example: "Juan"
            apellido:
              type: string
              example: "Perez"
            email:
              type: string
              example: "juan.perez@example.com"
    responses:
      200:
        description: Usuario actualizado exitosamente
        examples:
          application/json: {"usuario_id": 1, "nombre": "Juan", "apellido": "Perez"}
      404:
        description: Usuario no encontrado
        examples:
          application/json: {"error": "Usuario no encontrado"}
    """
    data = request.get_json()
    response, status = usuarios_service.update_usuario(id, data)
    return jsonify(response), status

@usuarios_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario_route(id):
    """
    Eliminar un usuario existente
    ---
    tags:
      - usuarios
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del usuario
    responses:
      200:
        description: Usuario eliminado exitosamente
        examples:
          application/json: {"message": "Usuario eliminado"}
      404:
        description: Usuario no encontrado
        examples:
          application/json: {"error": "Usuario no encontrado"}
    """
    response, status = usuarios_service.delete_usuario(id)
    return jsonify(response), status
