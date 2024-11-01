import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///loja.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-padrao'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secreta'
