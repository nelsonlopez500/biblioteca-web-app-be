from flask import Blueprint, request, jsonify
from app.services.categorias.categoriasService import categorias_service

categorias_bp = Blueprint('categorias', __name__)

@categorias_bp.route('/categorias', methods=['POST'])
def create_categoria_route():
    """
    Crear una nueva categoría
    ---
    tags:
      - categorias
    parameters:
      - in: body
        name: body
        required: True
        schema:
          id: Categoria
          required:
            - nombre
          properties:
            nombre:
              type: string
              example: "Nueva Categoria"
    responses:
      201:
        description: Categoría creada exitosamente
        examples:
          application/json: {"id": 1, "nombre": "Nueva Categoria"}
    """
    data = request.get_json()
    response, status = categorias_service.create_categoria(data)
    return jsonify(response), status

@categorias_bp.route('/categorias', methods=['GET'])
def get_categorias_route():
    """
    Obtener todas las categorías
    ---
    tags:
      - categorias
    responses:
      200:
        description: Lista de todas las categorías
        examples:
          application/json: [
            {"id": 1, "nombre": "Categoria 1"},
            {"id": 2, "nombre": "Categoria 2"}
          ]
    """
    response, status = categorias_service.get_categorias()
    return jsonify(response), status

@categorias_bp.route('/categorias/<int:id>', methods=['GET'])
def get_categoria_route(id):
    """
    Obtener una categoría por ID
    ---
    tags:
      - categorias
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID de la categoría
    responses:
      200:
        description: Categoría obtenida exitosamente
        examples:
          application/json: {"id": 1, "nombre": "Categoria 1"}
      404:
        description: Categoría no encontrada
        examples:
          application/json: {"error": "Categoría no encontrada"}
    """
    response, status = categorias_service.get_categoria(id)
    return jsonify(response), status

@categorias_bp.route('/categorias/<int:id>', methods=['PUT'])
def update_categoria_route(id):
    """
    Actualizar una categoría existente
    ---
    tags:
      - categorias
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID de la categoría
      - in: body
        name: body
        required: True
        schema:
          id: Categoria
          required:
            - nombre
          properties:
            nombre:
              type: string
              example: "Categoria Actualizada"
    responses:
      200:
        description: Categoría actualizada exitosamente
        examples:
          application/json: {"id": 1, "nombre": "Categoria Actualizada"}
      404:
        description: Categoría no encontrada
        examples:
          application/json: {"error": "Categoría no encontrada"}
    """
    data = request.get_json()
    response, status = categorias_service.update_categoria(id, data)
    return jsonify(response), status

@categorias_bp.route('/categorias/<int:id>', methods=['DELETE'])
def delete_categoria_route(id):
    """
    Eliminar una categoría existente
    ---
    tags:
      - categorias
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID de la categoría
    responses:
      200:
        description: Categoría eliminada exitosamente
        examples:
          application/json: {"message": "Categoría eliminada"}
      404:
        description: Categoría no encontrada
        examples:
          application/json: {"error": "Categoría no encontrada"}
    """
    response, status = categorias_service.delete_categoria(id)
    return jsonify(response), status