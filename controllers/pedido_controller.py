from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.pedido import Pedido, DetalhePedido
from models.produto import Produto
from models import db
from datetime import datetime

pedido_bp = Blueprint('pedido', __name__)

# Rota para criar um novo pedido
@pedido_bp.route('/pedidos', methods=['POST'])
@jwt_required()
def criar_pedido():
    data = request.json
    novo_pedido = Pedido(cliente_id=data['cliente_id'], data_compra=datetime.utcnow())
    db.session.add(novo_pedido)
    db.session.commit()
    return jsonify({'id': novo_pedido.pedido_id, 'cliente_id': novo_pedido.cliente_id}), 201

# Rota para listar todos os pedidos
@pedido_bp.route('/pedidos', methods=['GET'])
@jwt_required()
def listar_pedidos():
    pedidos = Pedido.query.all()
    pedidos_lista = [{'id': p.pedido_id, 'cliente_id': p.cliente_id, 'data': p.data_compra} for p in pedidos]
    return jsonify(pedidos_lista), 200

# Rota para adicionar um produto ao pedido
@pedido_bp.route('/pedidos/<int:pedido_id>/produtos', methods=['POST'])
@jwt_required()
def adicionar_produto_pedido(pedido_id):
    data = request.json
    produto_id = data['produto_id']
    valor = data['valor']
    desconto = data.get('desconto', 0.0)

    # Verifica se o pedido existe
    pedido = Pedido.query.get(pedido_id)
    if not pedido:
        return jsonify({'msg': 'Pedido não encontrado'}), 404

    # Verifica se o produto existe
    produto = Produto.query.get(produto_id)
    if not produto:
        return jsonify({'msg': 'Produto não encontrado'}), 404

    # Cria o detalhe do pedido
    detalhe_pedido = DetalhePedido(
        dt_pedido_id=pedido_id,
        dt_produto_id=produto_id,
        dt_valor=valor,
        dt_desconto=desconto
    )
    db.session.add(detalhe_pedido)
    db.session.commit()

    return jsonify({
        'id': detalhe_pedido.dt_id,
        'pedido_id': detalhe_pedido.dt_pedido_id,
        'produto_id': detalhe_pedido.dt_produto_id,
        'valor': detalhe_pedido.dt_valor,
        'desconto': detalhe_pedido.dt_desconto
    }), 201
