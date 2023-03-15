"""application entry point"""
from flask import Flask
from .models.db import DBClient


# Initializing flask app
app = Flask(__name__)

# Initializing database configurations

Db = DBClient(host='localhost', port=5233,
              user='postgres', password='postgres', db='postgres', app=app)
migrate = Db.get_migrate()
database = Db.get_engine()


# Route for seeing a data
@app.route('/')
def initial():
    """initial route
    welcome route

    Returns:
        _object_: welcome parameters
    """

    return {
        "message": "welcome to the Our Platform",
        "company": "RestaurantOne",
        "location": "Kampala",
        "year": 2023,
        "month": "March",
        "Country": "Uganda",
        "Project": "Alx-webstack project",
        "supervisor": "Alx-SE Mentors",
    }


# Running app
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
