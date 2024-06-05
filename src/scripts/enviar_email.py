from unidecode import unidecode
from smtplib import SMTP_SSL
from dotenv import load_dotenv
from os import getenv

load_dotenv()
email_remetente = getenv('EMAIL')
email_remetente_senha = getenv('SENHA')

server = SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(email_remetente, email_remetente_senha)


def enviar(email_destinatarios:list, mensagems_destinarios:list):
    for (email, mensagem)  in zip(email_destinatarios, mensagems_destinarios):
        mensagem = unidecode(mensagem)
        server.sendmail(email_remetente, email, mensagem)
    
    return f"Email(s) enviado(s) com sucesso para(os) {email_destinatarios}"