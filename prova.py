import tkinter as tk
from tkinter import messagebox

# exibir a mensagem
def enviar_mensagem():
    nome = entrada_nome.get()
    mensagem = entrada_mensagem.get()
    
    if nome and mensagem:
        janela_mensagem = tk.Toplevel()
        janela_mensagem.title("Mensagem Enviada")
        
        label_nome = tk.Label(janela_mensagem, text=f"Nome: {nome}")
        label_nome.pack()
        
        label_mensagem = tk.Label(janela_mensagem, text=f"Mensagem: {mensagem}")
        label_mensagem.pack()
    else:
        messagebox.showerror("Erro", "Por favor, preencha ambos os campos!")

#  janela principal
janela = tk.Tk()
janela.title("Envio de Mensagem")

# quem fez
label_autor = tk.Label(janela, text="Feito por [João Paulo]")
label_autor.pack()

# campo de nome
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()

# campo de mensagem
label_mensagem = tk.Label(janela, text="Mensagem:")
label_mensagem.pack()

entrada_mensagem = tk.Entry(janela)
entrada_mensagem.pack()

# botão de envio
botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem)
botao_enviar.pack()

janela.mainloop()