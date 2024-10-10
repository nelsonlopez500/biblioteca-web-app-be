from flask import Blueprint, request, jsonify
from app.services.editoriales.editorialesService import editoriales_service

editoriales_bp = Blueprint('editoriales', __name__)

@editoriales_bp.route('/editoriales', methods=['POST'])
def create_editorial_route():
    """
    Crear una nueva editorial
    ---
    tags:
      - editoriales
    parameters:
      - in: body
        name: body
        required: True
        schema:
          id: Editorial
          required:
            - nombre_editorial
          properties:
            nombre_editorial:
              type: string
              example: "Nueva Editorial"
    responses:
      201:
        description: Editorial creada exitosamente
        examples:
          application/json: {"editorial_id": 1, "nombre_editorial": "Nueva Editorial"}
    """
    data = request.get_json()
    response, status = editoriales_service.create_editorial(data)
    return jsonify(response), status

@editoriales_bp.route('/editoriales', methods=['GET'])
def get_editoriales_route():
    """
    Obtener todas las editoriales
    ---
    tags:
      - editoriales
    responses:
      200:
        description: Lista de todas las editoriales
        examples:
          application/json: [
            {"editorial_id": 1, "nombre_editorial": "Editorial 1"},
            {"editorial_id": 2, "nombre_editorial": "Editorial 2"}
          ]
    """
    response, status = editoriales_service.get_editoriales()
    return jsonify(response), status

@editoriales_bp.route('/editoriales/<int:id>', methods=['GET'])
def get_editorial_route(id):
    """
    Obtener una editorial por ID
    ---
    tags:
      - editoriales
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID de la editorial
    responses:
      200:
        description: Editorial obtenida exitosamente
        examples:
          application/json: {"editorial_id": 1, "nombre_editorial": "Editorial 1"}
      404:
        description: Editorial no encontrada
        examples:
          application/json: {"error": "Editorial no encontrada"}
    """
    response, status = editoriales_service.get_editorial(id)
    return jsonify(response), status

@editoriales_bp.route('/editoriales/<int:id>', methods=['PUT'])
def update_editorial_route(id):
    """
    Actualizar una editorial existente
    ---
    tags:
      - editoriales
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID de la editorial
      - in: body
        name: body
        required: True
        schema:
          id: Editorial
          required:
            - nombre_editorial
          properties:
            nombre_editorial:
              type: string
              example: "Editorial Actualizada"
    responses:
      200:
        description: Editorial actualizada exitosamente
        examples:
          application/json: {"editorial_id": 1, "nombre_editorial": "Editorial Actualizada"}
      404:
        description: Editorial no encontrada
        examples:
          application/json: {"error": "Editorial no encontrada"}
    """
    data = request.get_json()
    response, status = editoriales_service.update_editorial(id, data)
    return jsonify(response), status

@editoriales_bp.route('/editoriales/<int:id>', methods=['DELETE'])
def delete_editorial_route(id):
    """
    Eliminar una editorial existente
    ---
    tags:
      - editoriales
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID de la editorial
    responses:
      200:
        description: Editorial eliminada exitosamente
        examples:
          application/json: {"message": "Editorial eliminada"}
      404:
        description: Editorial no encontrada
        examples:
          application/json: {"error": "Editorial no encontrada"}
    """
    response, status = editoriales_service.delete_editorial(id)
    return jsonify(response), status
