from . import db

class Questao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(200), nullable=False)
    resposta_correta = db.Column(db.String(100), nullable=False)
    alternativas = db.relationship('Alternativa', backref='questao', lazy=True)

class Alternativa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(100), nullable=False)
    questao_id = db.Column(db.Integer, db.ForeignKey('questao.id'), nullable=False)
