import csv

def carregar_questoes(arquivo_csv):
    questoes = []
    with open(arquivo_csv, mode='r', encoding='utf-8') as file:
        leitor_csv = csv.DictReader(file)
        for linha in leitor_csv:
            questoes.append({
                'pergunta': linha['Pergunta'],
                'alternativas': [linha['Alternativa1'], linha['Alternativa2'], linha['Alternativa3'], linha['Alternativa4']],
                'resposta_correta': linha['Resposta Correta'],
                'explicacao': linha.get('Explicação', 'Sem explicação disponível.'),
                'categoria': linha['Categoria']
            })
    return questoes
