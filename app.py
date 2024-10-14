from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Olá, mundo!"

if __name__ == '__main__':
    app.run(debug=True)