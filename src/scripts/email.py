import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromaddr = 'ens-thiagofachini@ugv.edu.br'
password = 'F4chini_0312' 

toaddrs  = prompt("To: ").split()

print("Enter message")

# Construindo a mensagem
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is", len(msg))

# Configurando o servidor SMTP do Gmail
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(fromaddr, password)

# Enviando o e-mail
server.sendmail(fromaddr, toaddrs, msg)

# Finalizando a conexão
server.quit()