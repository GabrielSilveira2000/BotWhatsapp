
from src.routes import email, whatsapp
from flask import Flask
from flask_cors import CORS, cross_origin



app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config["CORS_HEADERS"] = "Content-Type"
app.register_blueprint(email.app_email)
app.register_blueprint(whatsapp.app_whatsapp)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port="3000")