from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.usuario import Usuario
from models import db
from werkzeug.security import generate_password_hash, check_password_hash

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    senha_hash = generate_password_hash(data['senha'])
    novo_usuario = Usuario(usuario_login=data['login'], usuario_senha=senha_hash, is_admin=data.get('is_admin', False))
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'id': novo_usuario.usuario_id, 'login': novo_usuario.usuario_login}), 201

@usuario_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = Usuario.query.filter_by(usuario_login=data['login']).first()

    if not usuario or not check_password_hash(usuario.usuario_senha, data['senha']):
        return jsonify({'msg': 'Login ou senha incorretos'}), 401

    access_token = create_access_token(identity={'id': usuario.usuario_id, 'is_admin': usuario.is_admin})
    return jsonify(access_token=access_token), 200

@usuario_bp.route('/usuarios', methods=['GET'])
@jwt_required()
def listar_usuarios():
    current_user = get_jwt_identity()
    if not current_user.get('is_admin'):
        return jsonify({'msg': 'Acesso negado'}), 403

    usuarios = Usuario.query.all()
    resultado = [{'id': u.usuario_id, 'login': u.usuario_login} for u in usuarios]
    return jsonify(resultado), 200
