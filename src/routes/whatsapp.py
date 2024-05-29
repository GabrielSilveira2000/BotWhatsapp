from src.scripts.enviar_mensagem_whatsapp import enviar
from flask import Blueprint, request

app_whatsapp = Blueprint('whatsapp', __name__)


@app_whatsapp.route("/api/whatsapp/mensagem/enviar", methods=["POST"])
def enviar_mensagem():
  requisicao = request.json
  return enviar(contatos=requisicao['contatos'], mensagens=requisicao['mensagens'], arquivos=requisicao['arquivos'])