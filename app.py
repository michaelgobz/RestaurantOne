"""application entry point"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.routes import views

# Initializing flask app
app = Flask(__name__)
app.secret_key = '8445a9af69bccd13de1a10de1de88158'

# Initializing database with flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/restaurantOne'
db = SQLAlchemy(app)

# Route registration
app.register_blueprint(views)

# Running app
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
