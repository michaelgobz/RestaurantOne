"""application entry point
    """

from os import getenv
from flask import Flask
from dotenv import load_dotenv
from api.routes import views

load_dotenv()
  
# Initializing flask app
app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

# Registering the routes
app.register_blueprint(views)

# Running app
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
