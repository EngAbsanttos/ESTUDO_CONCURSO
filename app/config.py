import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'  # Usando SQLite como padrão
    SQLALCHEMY_TRACK_MODIFICATIONS = False
