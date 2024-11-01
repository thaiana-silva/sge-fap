from . import db

class Produto(db.Model):
    __tablename__ = 'produtos'

    produto_id = db.Column(db.Integer, primary_key=True)
    produto_nome = db.Column(db.String(100), nullable=False)
    produto_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id_categoria'), nullable=False)

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id_categoria = db.Column(db.Integer, primary_key=True)
    nome_categoria = db.Column(db.String(50), nullable=False)
