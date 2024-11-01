from . import db
from datetime import datetime

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    pedido_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'), nullable=False)
    data_compra = db.Column(db.DateTime, default=datetime.utcnow)

class DetalhePedido(db.Model):
    __tablename__ = 'detalhes_pedido'

    dt_id = db.Column(db.Integer, primary_key=True)
    dt_pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'), nullable=False)
    dt_produto_id = db.Column(db.Integer, db.ForeignKey('produtos.produto_id'), nullable=False)
    dt_valor = db.Column(db.Float, nullable=False)
    dt_desconto = db.Column(db.Float, nullable=True)
