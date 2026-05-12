from flask import Flask
from routes.jogo_routes import jogo_bp

app = Flask(__name__)
app.register_blueprint(jogo_bp)

if __name__ == "__main__":
    app.run(debug=True)
