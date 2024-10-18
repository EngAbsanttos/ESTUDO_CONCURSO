import json
from flask import Flask, jsonify

app = Flask(__name__)

# Caminho para o arquivo JSON
QUESTOES_FILE = 'app/questoes.json'

def carregar_questoes():
    with open(QUESTOES_FILE, 'r') as f:
        return json.load(f)

@app.route('/questoes')
def get_questoes():
    questoes = carregar_questoes()
    return jsonify(questoes)

if __name__ == '__main__':
    app.run(debug=True)