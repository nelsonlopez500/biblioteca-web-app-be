from flask import Blueprint, request, jsonify
from app.services.prestamos.prestamosService import prestamos_service

prestamos_bp = Blueprint('prestamos', __name__)

@prestamos_bp.route('/prestamos', methods=['POST'])
def create_prestamo_route():
    """
    Crear un nuevo préstamo
    ---
    tags:
      - prestamos
    parameters:
      - in: body
        name: body
        required: True
        schema:
          id: Prestamo
          required:
            - usuario_id
            - libro_id
            - fecha_prestamo
            - biblioteca_id
          properties:
            usuario_id:
              type: integer
              example: 1
            libro_id:
              type: integer
              example: 1
            fecha_prestamo:
              type: string
              format: date-time
              example: "2023-01-01T10:00:00Z"
            fecha_vencimiento:
              type: string
              format: date-time
              example: "2023-01-15T10:00:00Z"
            estado_prestamo:
              type: string
              example: "activo"
            biblioteca_id:
              type: integer
              example: 1
    responses:
      201:
        description: Préstamo creado exitosamente
        examples:
          application/json: {"message": "Préstamo creado exitosamente"}
    """
    data = request.get_json()
    response, status = prestamos_service.create_prestamo(data)
    return jsonify(response), status

@prestamos_bp.route('/prestamos', methods=['GET'])
def get_prestamos_route():
    """
    Obtener todos los préstamos
    ---
    tags:
      - prestamos
    responses:
      200:
        description: Lista de todos los préstamos
        examples:
          application/json: [
            {"prestamo_id": 1, "usuario_id": 1, "libro_id": 1, "fecha_prestamo": "2023-01-01T10:00:00Z"},
            {"prestamo_id": 2, "usuario_id": 2, "libro_id": 2, "fecha_prestamo": "2023-01-02T10:00:00Z"}
          ]
    """
    response, status = prestamos_service.get_prestamos()
    return jsonify(response), status

@prestamos_bp.route('/prestamos/<int:id>', methods=['GET'])
def get_prestamo_route(id):
    """
    Obtener un préstamo por ID
    ---
    tags:
      - prestamos
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del préstamo
    responses:
      200:
        description: Préstamo obtenido exitosamente
        examples:
          application/json: {"prestamo_id": 1, "usuario_id": 1, "libro_id": 1, "fecha_prestamo": "2023-01-01T10:00:00Z"}
      404:
        description: Préstamo no encontrado
        examples:
          application/json: {"error": "Préstamo no encontrado"}
    """
    response, status = prestamos_service.get_prestamo(id)
    return jsonify(response), status

@prestamos_bp.route('/prestamos/<int:id>', methods=['PUT'])
def update_prestamo_route(id):
    """
    Actualizar un préstamo existente
    ---
    tags:
      - prestamos
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del préstamo
      - in: body
        name: body
        required: True
        schema:
          id: Prestamo
          required:
            - usuario_id
            - libro_id
            - fecha_prestamo
            - biblioteca_id
          properties:
            usuario_id:
              type: integer
              example: 1
            libro_id:
              type: integer
              example: 1
            fecha_prestamo:
              type: string
              format: date-time
              example: "2023-01-01T10:00:00Z"
            fecha_vencimiento:
              type: string
              format: date-time
              example: "2023-01-15T10:00:00Z"
            estado_prestamo:
              type: string
              example: "activo"
            biblioteca_id:
              type: integer
              example: 1
    responses:
      200:
        description: Préstamo actualizado exitosamente
        examples:
          application/json: {"message": "Préstamo actualizado exitosamente "}
      404:
        description: Préstamo no encontrado
        examples:
          application/json: {"error": "Préstamo no encontrado"}
    """
    data = request.get_json()
    response, status = prestamos_service.update_prestamo(id, data)
    return jsonify(response), status

@prestamos_bp.route('/prestamos/<int:id>', methods=['DELETE'])
def delete_prestamo_route(id):
    """
    Eliminar un préstamo existente
    ---
    tags:
      - prestamos
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del préstamo
    responses:
      200:
        description: Préstamo eliminado exitosamente
        examples:
          application/json: {"message": "Préstamo eliminado"}
      404:
        description: Préstamo no encontrado
        examples:
          application/json: {"error": "Préstamo no encontrado"}
    """
    response, status = prestamos_service.delete_prestamo(id)
    return jsonify(response), status