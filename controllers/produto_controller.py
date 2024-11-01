from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.produto import Produto, Categoria
from models import db

produto_bp = Blueprint('produto', __name__)

# Rota para adicionar um novo produto
@produto_bp.route('/produtos', methods=['POST'])
@jwt_required()
def criar_produto():
    data = request.json
    novo_produto = Produto(produto_nome=data['nome'], produto_categoria=data['categoria'])
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({'id': novo_produto.produto_id, 'nome': novo_produto.produto_nome}), 201

# Rota para listar todos os produtos
@produto_bp.route('/produtos', methods=['GET'])
@jwt_required()
def listar_produtos():
    produtos = Produto.query.all()
    produtos_lista = [{'id': p.produto_id, 'nome': p.produto_nome, 'categoria': p.produto_categoria} for p in produtos]
    return jsonify(produtos_lista), 200

# Rota para adicionar uma nova categoria
@produto_bp.route('/categorias', methods=['POST'])
@jwt_required()
def criar_categoria():
    data = request.json
    nova_categoria = Categoria(nome_categoria=data['nome'])
    db.session.add(nova_categoria)
    db.session.commit()
    return jsonify({'id': nova_categoria.id_categoria, 'nome': nova_categoria.nome_categoria}), 201

# Rota para listar todas as categorias
@produto_bp.route('/categorias', methods=['GET'])
@jwt_required()
def listar_categorias():
    categorias = Categoria.query.all()
    categorias_lista = [{'id': c.id_categoria, 'nome': c.nome_categoria} for c in categorias]
    return jsonify(categorias_lista), 200
