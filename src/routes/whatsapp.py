from src.scripts.enviar_mensagem_whatsapp import enviar
from flask import Blueprint, request
from re import sub

app_whatsapp = Blueprint('whatsapp', __name__)


@app_whatsapp.route("/api/whatsapp/mensagem/enviar", methods=["POST"])
def enviar_mensagem():
  requisicao = request.json
  contato = [contato for contato in requisicao['contatos'] if not contato == "" and not contato.isspace()]
  return enviar(contatos=contato, mensagens=requisicao['mensagens'], arquivos=requisicao['arquivos'])