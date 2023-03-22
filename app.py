"""application entry point"""
from os import getenv
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from api.core.base import Db as db
from api.routes import api

# load environment variables from .env file
load_dotenv()

# Initializing flask app
app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')

# Initializing CORS for cross origin requests
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)


# initializing database with flask app
db.initialize_app(app)

# Route for seeing a data
app.register_blueprint(api)


# Running app
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
