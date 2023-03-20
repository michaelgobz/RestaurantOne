"""application entry point"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# Initializing flask app
app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')

# Initializing database with flask app
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

# Route registration
from api.routes import *

# Running app
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
