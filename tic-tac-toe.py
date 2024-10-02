import tkinter as tk
from tkinter import messagebox

# Função para iniciar o jogo
def iniciar_jogo():
    global jogador_atual, jogadas
    jogador_atual = "X"  # O jogador "X" começa o jogo
    jogadas = [""] * 9  # Lista que armazenará as jogadas
    atualizar_interface()

# Função para atualizar o tabuleiro
def atualizar_interface():
    for i in range(9):
        botoes[i].config(text=jogadas[i], state=tk.NORMAL if jogadas[i] == "" else tk.DISABLED)

# Função para processar a jogada
def jogar(posicao):
    global jogador_atual
    if jogadas[posicao] == "":
        jogadas[posicao] = jogador_atual
        atualizar_interface()
        if verificar_vencedor():
            messagebox.showinfo("Fim de jogo", f"Jogador {jogador_atual} venceu!")
            reiniciar_jogo()
        elif "" not in jogadas:
            messagebox.showinfo("Fim de jogo", "Empate!")
            reiniciar_jogo()
        jogador_atual = "O" if jogador_atual == "X" else "X"  # Alternar jogadores

# Função para verificar se há um vencedor
def verificar_vencedor():
    combinacoes = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6)]
    for a, b, c in combinacoes:
        if jogadas[a] == jogadas[b] == jogadas[c] and jogadas[a] != "":
            return True
    return False

# Função para reiniciar o jogo
def reiniciar_jogo():
    iniciar_jogo()

# Configurações da interface gráfica
root = tk.Tk()
root.title("Jogo da Velha")
root.geometry("300x350")
jogador_atual = "X"
jogadas = [""] * 9

# Criar botões para o tabuleiro
botoes = []
for i in range(9):
    botao = tk.Button(root, text="", font="Arial 20", width=5, height=2, 
                      command=lambda i=i: jogar(i))
    botao.grid(row=i//3, column=i%3)
    botoes.append(botao)

# Botão para reiniciar o jogo
btn_reiniciar = tk.Button(root, text="Reiniciar Jogo", font="Arial 12", command=reiniciar_jogo)
btn_reiniciar.grid(row=3, column=0, columnspan=3)

# Iniciar o jogo
iniciar_jogo()

root.mainloop()
