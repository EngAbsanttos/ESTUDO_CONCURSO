from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados
engine = create_engine('mysql+pymysql://usuario:senha@localhost/meus_scripts')
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Modelo da tabela scripts
class Script(Base):
    __tablename__ = 'scripts'
    id = Column(Integer, primary_key=True)
    nome_do_tema = Column(String(100), unique=True)
    conteudo_sql = Column(Text)

# Função para salvar o script
def salvar_script(nome_tema, conteudo_sql):
    session = Session()
    script = session.query(Script).filter_by(nome_do_tema=nome_tema).first()
    if script:
        script.conteudo_sql = conteudo_sql
    else:
        script = Script(nome_do_tema=nome_tema, conteudo_sql=conteudo_sql)
        session.add(script)
    session.commit()

# Função para criar um novo banco de dados (Exemplo para MySQL)
def criar_novo_banco(nome_tema):
    engine.execute(f"CREATE DATABASE {nome_tema}")

# Exemplo de uso
nome_tema = "meu_tema"
conteudo_sql = "SELECT * FROM minha_tabela;"

# Verifica se o script já existe e salva ou cria um novo banco
salvar_script(nome_tema, conteudo_sql)
criar_novo_banco(nome_tema)  # Chame essa função apenas se quiser criar um novo banco