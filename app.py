from flask import Flask
from cliente_service import cliente_service

app = Flask(__name__)
app.register_blueprint(cliente_service)

if __name__ == '__main__':
    app.run(debug=True)
