from . import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    usuario_id = db.Column(db.Integer, primary_key=True)
    usuario_login = db.Column(db.String(80), unique=True, nullable=False)
    usuario_senha = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)