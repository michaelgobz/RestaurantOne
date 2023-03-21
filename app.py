"""application entry point"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()
from flask_cors import CORS

# models
from api.core.base import Db as db
from api.routes import api

# Initializing flask app
app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')

# Initializing CORS for cross origin requests
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

# models

# initializing database with flask app
db.initialize_app(app)

# Route for seeing a data
app.register_blueprint(api)


# Running app
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
