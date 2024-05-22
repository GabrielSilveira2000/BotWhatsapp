from flask import Blueprint

app_whatsapp = Blueprint('whatsapp', __name__)


@app_whatsapp.route("/api/whatsapp/mensagem/enviar", methods=["POST"])
def enviarMensagem():
  return "Mensagem enviada com sucesso!"

