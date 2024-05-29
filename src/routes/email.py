from src.scripts.enviar_email import enviar
from flask import Blueprint, request

app_email = Blueprint('email', __name__)


@app_email.route("/api/email/mensagem/enviar", methods=["POST"])
def enviarMensagem():
  requisicao = request.json
  return enviar(requisicao['email_remetente'], requisicao['mensagem'])