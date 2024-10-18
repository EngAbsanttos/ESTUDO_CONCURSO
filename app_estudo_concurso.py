import tkinter as tk
from tkinter import messagebox
from carregar_questoes import carregar_questoes

# Agora você pode usar a função para carregar o CSV
questoes = carregar_questoes('questoes.csv')


class EstudoConcursoApp:
    def __init__(self, master, questoes):
        self.master = master
        self.questoes = questoes
        self.indice_atual = 0
        
        # Criação dos widgets
        self.pergunta_label = tk.Label(master, text="")
        self.pergunta_label.pack(pady=10)
        
        self.var_alternativa = tk.StringVar()
        self.opcoes = [tk.Radiobutton(master, text="", variable=self.var_alternativa, value=str(i)) for i in range(4)]
        for opcao in self.opcoes:
            opcao.pack(anchor='w')
        
        self.botao_responder = tk.Button(master, text="Responder", command=self.verificar_resposta)
        self.botao_responder.pack(pady=10)
        
        self.botao_proxima = tk.Button(master, text="Próxima Questão", command=self.proxima_questao)
        self.botao_proxima.pack(pady=10)
        
        # Carregar primeira questão
        self.mostrar_questao()

    def mostrar_questao(self):
        questao = self.questoes[self.indice_atual]
        self.pergunta_label.config(text=questao['pergunta'])
        for i, alternativa in enumerate(questao['alternativas']):
            self.opcoes[i].config(text=alternativa, value=alternativa)
        self.var_alternativa.set(None)  # Resetar seleção

    def verificar_resposta(self):
        questao = self.questoes[self.indice_atual]
        resposta = self.var_alternativa.get()
        if resposta == questao['resposta_correta']:
            messagebox.showinfo("Correto!", "Você acertou!")
        else:
            messagebox.showinfo("Errado", f"Resposta incorreta.\nExplicação: {questao['explicacao']}")

    def proxima_questao(self):
        self.indice_atual = (self.indice_atual + 1) % len(self.questoes)
        self.mostrar_questao()

# Main
if __name__ == "__main__":
    arquivo_csv = 'questoes.csv'  # Coloque o caminho correto para o seu CSV
    questoes = carregar_questoes(arquivo_csv)
    
    root = tk.Tk()
    app = EstudoConcursoApp(root, questoes)
    root.mainloop()
