import smtplib

def prompt(prompt):
    return input(prompt).strip()

# Dados do remetente
fromaddr = 'thiagofachini787878@gmail.com'  # Seu endereço de e-mail do Gmail
password = 'F4chini_0312'  # Sua senha do Gmail

# Dados do destinatário
toaddrs  = prompt("To: ").split()

print("Enter message, end with ^D (Unix) or ^Z (Windows):")

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