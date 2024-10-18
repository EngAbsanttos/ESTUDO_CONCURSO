# models.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, JSON, ForeignKey

# Cria a conexão com o banco de dados
engine = create_engine('mysql+pymysql://usuario:senha@localhost/estudo_concurso')
Base = declarative_base()

# Define os modelos das tabelas
class Tema(Base):
    __tablename__ = 'temas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)

class Questao(Base):
    __tablename__ = 'questoes'
    id = Column(Integer, primary_key=True)
    pergunta = Column(Text)
    alternativas = Column(JSON)
    resposta_correta = Column(Integer)
    tema_id = Column(Integer, ForeignKey('temas.id'))
    tema = relationship("Tema")

# Cria as tabelas no banco de dados (se necessário)
Base.metadata.create_all(engine)