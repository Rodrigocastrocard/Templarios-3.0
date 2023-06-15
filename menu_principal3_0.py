from tkinter import*

def cadastro ():
    janela.destroy()
    import tela_menu_cadastro

def financeiro():
    janela.destroy()
    import tela_menu_financeiro

def configuracao():
    janela.destroy()
    import tela_menu_configuracao




janela = Tk()
janela.title("MENU PRINCIPAL")
janela.state("zoomed")
#texto = Label(janela, text="Clique em cadastrar, para incluir um novo cadastro")
#texto.grid(column=0, row=0, padx=10, pady=10)

'''

#importar imagem
img_tela = PhotoImage(file="images\\telatemp.png")

#criando labels
lab_fundo=Label(janela, image=img_tela)
lab_fundo.pack()

'''


botao_cadastro = Button(janela, text='CADASTROS', command= cadastro)
botao_cadastro.place(width=130, height=50, x=0, y=0)
botao_financeiro = Button(janela, text="FINANCEIRO", command= financeiro)
botao_financeiro.place(width=130, height=50, x=0, y=50)
botao_configuracao = Button(janela, text="CONFIGURACAO", command= configuracao)
botao_configuracao.place(width=130, height=50, x=0, y=100)
botao_voltar = Button(janela, text="SAIR", command= janela.destroy)
botao_voltar.place(width=130, height=50, x=0, y=150)



#texto_resposta = Label(janela, text="")
#texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
