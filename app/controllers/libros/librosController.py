from flask import Blueprint, request, jsonify
from app.services.libros.librosService import libros_service

libros_bp = Blueprint('libros', __name__)

@libros_bp.route('/libros', methods=['POST'])
def create_libro_route():
    """
    Crear un nuevo libro
    ---
    tags:
      - libros
    parameters:
      - in: body
        name: body
        required: True
        schema:
          id: Libro
          required:
            - titulo
            - isbn
            - fecha_publicacion
            - editorial_id
            - categoria_id
            - biblioteca_id
          properties:
            titulo:
              type: string
              example: "Título del Libro"
            isbn:
              type: string
              example: "978-3-16-148410-0"
            fecha_publicacion:
              type: string
              format: date
              example: "2023-01-01"
            editorial_id:
              type: integer
              example: 1
            categoria_id:
              type: integer
              example: 1
            biblioteca_id:
              type: integer
              example: 1
    responses:
      201:
        description: Libro creado exitosamente
        examples:
          application/json: {"libro_id": 1, "titulo": "Título del Libro"}
    """
    data = request.get_json()
    response, status = libros_service.create_libro(data)
    return jsonify(response), status

@libros_bp.route('/libros', methods=['GET'])
def get_libros_route():
    """
    Obtener todos los libros
    ---
    tags:
      - libros
    responses:
      200:
        description: Lista de todos los libros
        examples:
          application/json: [
            {"libro_id": 1, "titulo": "Título del Libro 1"},
            {"libro_id": 2, "titulo": "Título del Libro 2"}
          ]
    """
    response, status = libros_service.get_libros()
    return jsonify(response), status

@libros_bp.route('/libros/<int:id>', methods=['GET'])
def get_libro_route(id):
    """
    Obtener un libro por ID
    ---
    tags:
      - libros
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del libro
    responses:
      200:
        description: Libro obtenido exitosamente
        examples:
          application/json: {"libro_id": 1, "titulo": "Título del Libro 1"}
      404:
        description: Libro no encontrado
        examples:
          application/json: {"error": "Libro no encontrado"}
    """
    response, status = libros_service.get_libro(id)
    return jsonify(response), status

@libros_bp.route('/libros/<int:id>', methods=['PUT'])
def update_libro_route(id):
    """
    Actualizar un libro existente
    ---
    tags:
      - libros
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del libro
      - in: body
        name: body
        required: True
        schema:
          id: Libro
          required:
            - titulo
            - isbn
            - fecha_publicacion
            - editorial_id
            - categoria_id
            - biblioteca_id
          properties:
            titulo:
              type: string
              example: "Título Actualizado"
            isbn:
              type: string
              example: "978-3-16-148410-1"
            fecha_publicacion:
              type: string
              format: date
              example: "2023-02-01"
            editorial_id:
              type: integer
              example: 1
            categoria_id:
              type: integer
              example: 1
            biblioteca_id:
              type: integer
              example: 1
    responses:
      200:
        description: Libro actualizado exitosamente
        examples:
          application/json: {"libro_id": 1, "titulo": "Título Actualizado"}
      404:
        description: Libro no encontrado
        examples:
          application/json: {"error": "Libro no encontrado"}
    """
    data = request.get_json()
    response, status = libros_service.update_libro(id, data)
    return jsonify(response), status

@libros_bp.route('/libros/<int:id>', methods=['DELETE'])
def delete_libro_route(id):
    """
    Eliminar un libro existente
    ---
    tags:
      - libros
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del libro
    responses:
      200:
        description: Libro eliminado exitosamente
        examples:
          application/json: {"message": "Libro eliminado"}
      404:
        description: Libro no encontrado
        examples:
          application/json: {"error": "Libro no encontrado"}
    """
    response, status = libros_service.delete_libro(id)
    return jsonify(response), status
