import PySimpleGUI as sg
import mysql.connector

con = mysql.connector.connect(host='localhost',
                             database='templarios',
                             user='root',
                             password='Janete4353',
                             auth_plugin='mysql_native_password')

layout = [
    [sg.Text('USUARIO')],
    [sg.Input(key='usuario')],
    [sg.Text('senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]

busca = """select * from usuarios"""
cursor = con.cursor()
cursor.execute(busca)
linhas = cursor.fetchall()
print(linhas)
cursor.close()

window = sg.Window('Login',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        usuario_correto = 'a'
        senha_correta = 'a'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso! ')
            login = 1
            window.close()

        else:
            window['mensagem'].update('Usuario ou senha incorreto! ')

if login == 1:
    import menu_principal3_0



