from flask import Blueprint

app_email = Blueprint('email', __name__)


@app_email.route("/api/email/mensagem/enviar", methods=["POST"])
def enviarMensagem():
  return "Mensagem enviada com sucesso!"

