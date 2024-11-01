from .usuario_controller import usuario_bp
from .cliente_controller import cliente_bp
from .pedido_controller import pedido_bp
from .produto_controller import produto_bp

# Lista de blueprints para facilitar a importação e registro no app.py
__all__ = ["usuario_bp", "cliente_bp", "pedido_bp", "produto_bp"]
