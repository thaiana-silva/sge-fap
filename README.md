# Gerenciamento de Pedidos

Este é um projeto de API REST para gerenciamento de pedidos de uma loja online, desenvolvido com **Flask** e **SQLAlchemy**. Ele permite a administração de usuários, clientes, produtos, categorias e pedidos, com autenticação JWT para garantir segurança.

## Funcionalidades

- **Autenticação JWT**: Autenticação segura para usuários administradores.
- **CRUD Completo**: Manipulação de usuários, clientes, produtos, categorias e pedidos.
- **Relacionamento entre Entidades**: Pedidos contêm detalhes dos produtos e estão associados a clientes.
- **Sistema de Permissões**: Apenas administradores podem acessar certas rotas.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework para criação da API REST.
- **SQLAlchemy**: ORM para manipulação de banco de dados.
- **Flask-JWT-Extended**: Gerenciamento de autenticação via JWT.
- **SQLite**: Banco de dados relacional.

## Estrutura do Projeto
```
gerenciamento_pedidos/
├── app.py                    # Arquivo principal da aplicação
├── config.py                 # Configurações do banco de dados e JWT
├── /models                   # Modelos de banco de dados
│   ├── __init__.py           # Inicialização do SQLAlchemy
│   ├── usuario.py            # Modelo de usuário
│   ├── cliente.py            # Modelo de cliente
│   ├── pedido.py             # Modelo de pedido e detalhe do pedido
│   ├── produto.py            # Modelo de produto e categoria
├── /controllers              # Controladores de rotas da API
│   ├── __init__.py           # Inicialização dos blueprints
│   ├── usuario_controller.py # Rotas de usuário e login
│   ├── cliente_controller.py # Rotas de cliente
│   ├── pedido_controller.py  # Rotas de pedido
│   ├── produto_controller.py # Rotas de produto e categoria
└── loja.db                   # Banco de dados SQLite (gerado automaticamente)
```

## Rotas da API
### Usuários (Administradores)
- **POST /api/usuarios** - Cadastrar novo usuário administrador.
- **POST /api/login** - Autenticar usuário e receber token JWT.
- **GET /api/usuarios** - Listar todos os usuários (apenas para administradores).
### Clientes
- **POST /api/clientes** - Cadastrar novo cliente.
- **GET /api/clientes** - Listar todos os clientes.
### Produtos e Categorias
- **POST /api/produtos** - Adicionar novo produto.
- **GET /api/produtos** - Listar todos os produtos.
- **POST /api/categorias** - Adicionar nova categoria.
- **GET /api/categorias** - Listar todas as categorias.
### Pedidos
- **POST /api/pedidos** - Criar um novo pedido.
- **GET /api/pedidos** - Listar todos os pedidos.
- **POST /api/pedidos/<pedido_id>/produtos** - Adicionar produto a um pedido.

