from unidecode import unidecode
from smtplib import SMTP_SSL

email_remetente = 'ens-thiagofachini@ugv.edu.br'
email_remetente_senha = 'F4chini_0312'

server = SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(email_remetente, email_remetente_senha)


def enviar(email_destinatario:str, mensagem:str):
    mensagem = unidecode(mensagem)
    server.sendmail(email_remetente, email_destinatario, mensagem)
    
    return f"Email enviado com sucesso para {email_destinatario}"