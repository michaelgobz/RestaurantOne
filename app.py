"""application entry point"""
from flask import Flask
# models
from models.account import Address, User


# Initializing flask app
app = Flask(__name__)

# Initializing database configurations

# models
user = User()
address = Address()


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
