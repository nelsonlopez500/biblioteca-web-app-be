from flask import Blueprint, request, jsonify
from app.services.biblioteca.bibliotecaService import bibliotecas_service

bibliotecas_bp = Blueprint("bibliotecas", __name__)


@bibliotecas_bp.route("/bibliotecas", methods=["GET"])
def get_bibliotecas_route():
    """
    Obtener todas las bibliotecas
    ---
    tags:
      - bibliotecas
    responses:
      200:
        description: Lista de todas las bibliotecas
        examples:
          application/json: [
            {
              "biblioteca_id": 1,
              "nombre_biblioteca": "Biblioteca 1",
              "direccion": "Dirección 1",
              "telefono": "123456789",
              "email": "email1@example.com",
              "status": true,
              "created_at": "2024-10-06T12:59:58Z"
            },
            {
              "biblioteca_id": 2,
              "nombre_biblioteca": "Biblioteca 2",
              "direccion": "Dirección 2",
              "telefono": "987654321",
              "email": "email2@example.com",
              "status": true,
              "created_at": "2024-10-06T12:59:58Z"
            }
          ]
    """
    response, status = bibliotecas_service.get_bibliotecas()
    return jsonify(response), status


@bibliotecas_bp.route("/bibliotecas/<int:id>", methods=["GET"])
def get_biblioteca_route(id):
    """
    Obtener una biblioteca por ID
    ---
    tags:
      - bibliotecas
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID de la biblioteca
    responses:
      200:
        description: Biblioteca obtenida exitosamente
        examples:
          application/json: {
            "biblioteca_id": 1,
            "nombre_biblioteca": "BiblioTK",
            "direccion": "SA",
            "telefono": "2424-2424",
            "email": "bibliotk@email.com",
            "status": true,
            "created_at": "2024-10-06T12:59:58Z"
          }
      404:
        description: Biblioteca no encontrada
        examples:
          application/json: {"error": "Biblioteca no encontrada"}
    """
    response, status = bibliotecas_service.get_biblioteca(id)
    return jsonify(response), status