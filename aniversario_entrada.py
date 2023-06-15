import mysql.connector
from datetime import datetime
import win32com.client as win32


con = mysql.connector.connect(host='localhost',
                              database='templarios',
                              user='root',
                              password='Janete4353',
                              auth_plugin='mysql_native_password')

#funcao para enviar email
def enviaemail():
      # criar a integração com o outlook
      outlook = win32.Dispatch('outlook.application')

      # criar um email
      email = outlook.CreateItem(0)

      # configurar as informações do seu e-mail
      email.To = "miriamaraujo181@gmail.com;rodrigocastrocard@gmail.com;m.c.templarioslp@gmail.com"
      email.Subject = "Aniversariante de entrada, Moto Clube Templários"
      email.HTMLBody = f"""
           <p>Olá, aqui é o código Python do Rodrigo e estou rodando uma terefa automatica. </p>

            <p> Gostaria de te lembrar que o membro ! {aniversariantemc} ! está completando hoje mais um ano de Moto Clube Templarios. Ele entrou em  ! {dataentrada} ! </p>


            <p>Nao esqueca de parabenizar o membro ! {aniversariantemc} ! </p>

            <p>Abs,</p>
            <p>RCC System</p>
            """

      email.Send()

#consulta no banco de dados
consulta_sql = """select nomemembro, candidaturamembro from membros """
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()

#busca a data atual e formata para dia e mes
hoje = datetime.today()
today = hoje.strftime("%d/%m")

#compara a consulta do banco com a data atual
for linha in linhas:
    consulta = linha[1].strftime("%d/%m")
    if consulta == today:
        dataentrada = linha[1]
        aniversariantemc = linha[0]
        enviaemail()
        print('email enviado')
    else:
        print('erro')



