from flask import Blueprint, request, jsonify
from app.services.prestamos.prestamosHistorialService import prestamos_historial_service

prestamos_historial_bp = Blueprint("prestamos_historial", __name__)


@prestamos_historial_bp.route("/prestamos_historial", methods=["GET"])
def get_prestamos_historial_route():
    """
    Obtener todos los historiales de préstamos
    ---
    tags:
      - prestamos_historial
    responses:
      200:
        description: Lista de todos los historiales de préstamos
        examples:
          application/json: [
            {
              "historial_id": 1,
              "prestamo_id": 101,
              "fecha_accion": "2024-10-06T12:59:58Z",
              "accion": "Creación",
              "descripcion": "Préstamo creado exitosamente"
            },
            {
              "historial_id": 2,
              "prestamo_id": 102,
              "fecha_accion": "2024-10-07T12:00:00Z",
              "accion": "Actualización",
              "descripcion": "Préstamo actualizado exitosamente"
            }
          ]
    """
    response, status = prestamos_historial_service.get_prestamos_historial()
    return jsonify(response), status


@prestamos_historial_bp.route("/prestamos_historial/<int:id>", methods=["GET"])
def get_prestamo_historial_route(id):
    """
    Obtener un historial de préstamo por ID
    ---
    tags:
      - prestamos_historial
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del historial de préstamo
    responses:
      200:
        description: Historial de préstamo obtenido exitosamente
        examples:
          application/json: {
            "historial_id": 1,
            "prestamo_id": 101,
            "fecha_accion": "2024-10-06T12:59:58Z",
            "accion": "Creación",
            "descripcion": "Préstamo creado exitosamente"
          }
      404:
        description: Historial de préstamo no encontrado
        examples:
          application/json: {"error": "Historial de préstamo no encontrado"}
    """
    response, status = prestamos_historial_service.get_prestamo_historial(id)
    return jsonify(response), status