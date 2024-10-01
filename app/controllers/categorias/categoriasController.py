from flask import Blueprint, request, jsonify
from services.categorias.categoriasService import categorias_service

categorias_bp = Blueprint('categorias', __name__)

@categorias_bp.route('/categorias', methods=['POST'])
def create_categoria_route():
    data = request.get_json()
    response, status = categorias_service.create_categoria(data)
    return jsonify(response), status

@categorias_bp.route('/categorias', methods=['GET'])
def get_categorias_route():
    response, status = categorias_service.get_categorias()
    return jsonify(response), status

@categorias_bp.route('/categorias/<int:id>', methods=['GET'])
def get_categoria_route(id):
    response, status = categorias_service.get_categoria(id)
    return jsonify(response), status

@categorias_bp.route('/categorias/<int:id>', methods=['PUT'])
def update_categoria_route(id):
    data = request.get_json()
    response, status = categorias_service.update_categoria(id, data)
    return jsonify(response), status

@categorias_bp.route('/categorias/<int:id>', methods=['DELETE'])
def delete_categoria_route(id):
    response, status = categorias_service.delete_categoria(id)
    return jsonify(response), status