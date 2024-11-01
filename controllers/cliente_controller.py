from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.cliente import Cliente
from models import db

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/clientes', methods=['POST'])
@jwt_required()
def criar_cliente():
    data = request.json
    novo_cliente = Cliente(cliente_nome=data['nome'], cliente_email=data['email'])
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({'id': novo_cliente.cliente_id, 'nome': novo_cliente.cliente_nome}), 201

@cliente_bp.route('/clientes', methods=['GET'])
@jwt_required()
def listar_clientes():
    clientes = Cliente.query.all()
    clientes_lista = [{'id': c.cliente_id, 'nome': c.cliente_nome, 'email': c.cliente_email} for c in clientes]
    return jsonify(clientes_lista), 200
