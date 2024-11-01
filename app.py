from flask import Flask
from models import db
from flask_jwt_extended import JWTManager
from config import Config

# Inicializa a aplicação
app = Flask(__name__)
app.config.from_object(Config)

# Inicializa o banco de dados e JWT
db.init_app(app)
jwt = JWTManager(app)

# Importando e registrando os Blueprints
from controllers import usuario_bp, cliente_bp, pedido_bp, produto_bp

app.register_blueprint(usuario_bp, url_prefix='/api')
app.register_blueprint(cliente_bp, url_prefix='/api')
app.register_blueprint(pedido_bp, url_prefix='/api')
app.register_blueprint(produto_bp, url_prefix='/api')

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)


