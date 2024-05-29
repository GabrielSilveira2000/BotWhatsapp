
from src.routes import email
from flask import Flask


app = Flask(__name__)
app.register_blueprint(email.app_email)
# app.register_blueprint(whatsapp.app_whatsapp)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port="3000", debug=True)