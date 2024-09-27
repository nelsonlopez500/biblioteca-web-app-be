from flask import Blueprint, request, jsonify

ejemplos_bp = Blueprint('ejemplos', __name__)

# Ejemplo de datos en memoria
items = []

@ejemplos_bp.route('/items', methods=['GET'])
def get_items():
    """
    Obtener todos los items
    ---
    responses:
      200:
        description: Lista de todos los items
        examples:
          application/json: [
            {"id": 1, "nombre": "Item 1"},
            {"id": 2, "nombre": "Item 2"}
          ]
    """
    return jsonify(items), 200

@ejemplos_bp.route('/items', methods=['POST'])
def create_item():
    """
    Crear un nuevo item
    ---
    parameters:
      - in: body
        name: body
        required: True
        schema:
          id: Item
          required:
            - nombre
          properties:
            nombre:
              type: string
              example: "Nuevo Item"
    responses:
      201:
        description: Item creado exitosamente
        examples:
          application/json: {"id": 1, "nombre": "Nuevo Item"}
    """
    data = request.get_json()
    new_item = {
        'id': len(items) + 1,
        'nombre': data['nombre']
    }
    items.append(new_item)
    return jsonify(new_item), 201

@ejemplos_bp.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    """
    Actualizar un item existente
    ---
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del item
      - in: body
        name: body
        required: True
        schema:
          id: Item
          required:
            - nombre
          properties:
            nombre:
              type: string
              example: "Item Actualizado"
    responses:
      200:
        description: Item actualizado exitosamente
        examples:
          application/json: {"id": 1, "nombre": "Item Actualizado"}
    """
    data = request.get_json()
    for item in items:
        if item['id'] == id:
            item['nombre'] = data['nombre']
            return jsonify(item), 200
    return jsonify({'error': 'Item no encontrado'}), 404

@ejemplos_bp.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    """
    Eliminar un item existente
    ---
    parameters:
      - in: path
        name: id
        type: integer
        required: True
        description: ID del item
    responses:
      200:
        description: Item eliminado exitosamente
        examples:
          application/json: {"message": "Item eliminado"}
    """
    global items
    items = [item for item in items if item['id'] != id]
    return jsonify({'message': 'Item eliminado'}), 200