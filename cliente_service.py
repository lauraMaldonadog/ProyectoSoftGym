from flask import Blueprint, request, jsonify
from cliente import Cliente

cliente_service = Blueprint('cliente_service', __name__)

clientes = []

@cliente_service.route('/clientes', methods=['GET'])
def get_clientes():
    return jsonify([cliente.to_dict() for cliente in clientes])

@cliente_service.route('/clientes', methods=['POST'])
def agregar_cliente():
    datos_cliente = request.get_json()
    id_cliente_nuevo = datos_cliente.get('id')
    
    # Verificar si el cliente ya existe
    for cliente in clientes:
        if cliente.id == id_cliente_nuevo:
            return jsonify({'error': 'Cliente ya existe'}), 400
    
    cliente = Cliente(**datos_cliente)
    clientes.append(cliente)
    return jsonify(cliente.to_dict()), 201

@cliente_service.route('/clientes/<int:id_cliente>', methods=['PUT'])
def modificar_cliente(id_cliente):
    datos_modificados = request.get_json()
    for cliente in clientes:
        if cliente.id == id_cliente:
            cliente.__dict__.update(datos_modificados)
            return jsonify(cliente.to_dict())
    return jsonify({'error': 'Cliente no encontrado'}), 404

@cliente_service.route('/clientes/<int:id_cliente>', methods=['DELETE'])
def eliminar_cliente(id_cliente):
    for i, cliente in enumerate(clientes):
        if cliente.id == id_cliente:
            del clientes[i]
            return jsonify({'mensaje': 'Cliente eliminado correctamente'})
    return jsonify({'error': 'Cliente no encontrado'}), 404
