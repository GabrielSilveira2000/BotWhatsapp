
from flask import Flask, request

app = Flask(__name__)

@app.route("/enviarMensagem", methods=["POST"])
def enviarMensagem():
  return "Mensagem enviada com sucesso!"

@app.route("/enviarEmail", methods=["POST"])
def enviarEmail():
  return "Email enviado com sucesso!"

if __name__ == "__main__":
  app.run(debug=True)
