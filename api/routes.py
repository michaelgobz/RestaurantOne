from flask import request, jsonify, make_response, abort, redirect, Blueprint
from wtforms import Form, StringField, PasswordField, validators



from models.auth.auth import Auth
from models.store.restaurant import Restaurant
from models.products.product import Product
from models.menus.menu import Menu
from models.menus.menu_item import MenuItem
from models.orders.order import Order
from models.reservations.reservation import Reservation



AUTH = Auth()
RESTAURANT = Restaurant()
PRODUCT = Product()
MENU = Menu()
MENU_ITEM = MenuItem
ORDER = Order
RESERVATION = Reservation

views = Blueprint('views', __name__, url_prefix='/')

# Route for seeing a data
@views.route('/')
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

# class SignupForm(FlaskForm):
#     email = StringField('Email')
#     password = PasswordField('Password')

@views.route('/auth/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """Creates user
    """
    # form = SignupForm(request.form)

    # if not form.validate():
    #     return make_response(jsonify({"errors": form.errors}), 400)
    
    email = request.form['email']
    password = request.form['password']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    phone_number = request.form['phone_number']
    country = request.form['country']
    location = request.form['location']
    address = request.form['address']

    try:
        user = AUTH.register_user(email, password, firstname, lastname,
                                  phone_number, country, location, address)
    except ValueError:
        return make_response(jsonify({"message": "email already registered"}), 400)

    return jsonify({"email": user.email, "message": f"User {user.first_name} {user.last_name} created"})
    # return redirect('/auth/login')


@views.route('/auth/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Creates a session for the user and stores it as a cookie
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400

    # validate email format
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return jsonify({'error': 'Invalid email format.'}), 400

    # validate password strength
    min_password_length = 8
    if len(password) < min_password_length:
        return jsonify({'error': f'Password should be at least {min_password_length} characters long.'}), 400

    # check if email and password match the expected data format
    if not AUTH.valid_login(email, password):
        return jsonify({'error': 'Invalid email or password.'}), 401

    session_id = AUTH.create_session(email)
    if session_id is not None:
        response = jsonify({'email': email, 'message': "You were logged in successfully"})
        response.set_cookie('session_id', session_id)
        return response
        
    return jsonify({'error': 'Unable to create session.'}), 500


@views.route('/auth/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Destroys a session
    """
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect('/')

class ResetPasswordForm(Form):
    email = StringField('Email', [validators.InputRequired(), validators.Email()])


@views.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ Generates a token and responds with 200
    """

    form = ResetPasswordForm(request.form)

    if form.validate():
        email = request.form['email']

        # Check if email exists in system
        user = AUTH.get_user_by_email(email)
        if user is None:
            abort(404)

        # Generate reset password token and send email to user
        token = AUTH.get_reset_password_token(email)
        # Send email to user with reset password token

        return jsonify({'email': email, 'reset_token': token})
    else:
        abort(400)


# def validate_update_password_input(email, reset_token, new_pwd):
#     # Check if all required parameters are provided
#     if not email or not reset_token or not new_pwd:
#         return False

#     # Check if reset token is valid for the provided email
#     if not AUTH.is_valid_reset_token(email, reset_token):
#         return False

#     # Check if the new password is strong enough
#     if not is_strong_password(new_pwd):
#         return False

#     return True


@views.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ Updates password
    """
    try:
        email = request.form['email']
        reset_token = request.form['reset_token']
        new_pwd = request.form['new_password']
    except KeyError:
        abort(403)

    try:
        AUTH.update_password(reset_token, new_pwd)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "message": "Password updated"})


#### RESTAURANT ####

@views.route('/dashboard/new/restaurant', methods=['POST', 'GET'], strict_slashes=False)
def new_restaurant():
    """Creates a new restaurant
    """
    name = request.form.get('name')
    description = request.form.get('description')
    location = request.form.get('location')
    mission_statement = request.form.get('mission_statement')

    try:
        restaurant = RESTAURANT.register_restaurant(name, description, location, mission_statement)
    except ValueError:
        return make_response(jsonify({"message": "Restaurant already registered"}), 400)

    return jsonify({"restaurant": restaurant.name, "message": f"Restaurant {restaurant.name} created"})



#### PRODUCT ####

@views.route('/dashboard/new/product', methods=['POST', 'GET'], strict_slashes=False)
def new_product():
    """Creates a new product
    """
    short_name = request.form.get('short_name')
    long_name = request.form.get('long_name')
    description = request.form.get('description')
    category = request.form.get('category')
    owner = request.form.get('owner')
    price = request.form.get('price')
    varients = request.form.get('short_name')
    duration_of_preparation = request.form.get('duration_of_preparation')
    max_quantity = request.form.get('max_quantity')
    location = request.form.get('location')

    try:
        product = PRODUCT.register_menu(short_name, long_name, description, category, 
                                        owner, price, varients, duration_of_preparation, max_quantity, location)
    except ValueError:
        return make_response(jsonify({"message": "product already registered"}), 400)

    return jsonify({"product": product.short_name, "message": f"product {product.short_name} created"})



#### MENU ####

@views.route('/dashboard/new/menu', methods=['POST', 'GET'], strict_slashes=False)
def new_menu():
    """Creates a new menu
    """
    name = request.form.get('name')
    description = request.form.get('description')
    category = request.form.get('category')
    owner_restaurant_name = request.form.get('owner_restaurant_name')

    try:
        menu = MENU.register_menu(name, description, category, owner_restaurant_name)
    except ValueError:
        return make_response(jsonify({"message": "menu already registered"}), 400)

    return jsonify({"menu": menu.name, "message": f"menu {menu.name} created"})



#### MENU ITEM ####

@views.route('/dashboard/new/menu_item', methods=['POST', 'GET'], strict_slashes=False)
def new_menu_item():
    """Creates a new menu item
    """
    name = request.form.get('name')
    description = request.form.get('description')
    category = request.form.get('category')
    price = request.form.get('price')
    foods = request.form.get('foods')
    toppings = request.form.get('toppings')
    serving_model = request.form.get('serving_model')

    try:
        menu_item = MENU_ITEM.register_menu_item(name, description, category, price,
                                            foods, toppings, serving_model)
    except ValueError:
        return make_response(jsonify({"message": "Menu item already registered"}), 400)

    return jsonify({"menu_item": menu_item.name, "message": f"Menu item {menu_item.name} created"})



#### ORDER ####

@views.route('/dashboard/new/order', methods=['POST', 'GET'], strict_slashes=False)
def new_order():
    """Creates a new order
    """
    items = request.form.get('items')
    total_cart_price = request.form.get('total_cart_price')
    address = request.form.get('address')
    shipment_method = request.form.get('shipment_method')
    payment_method = request.form.get('payment_method')

    try:
        order = ORDER.register_order(items, total_cart_price, address,
                                    shipment_method, payment_method)
    except ValueError:
        return make_response(jsonify({"message": "order already registered"}), 400)

    return jsonify({"message": f"The total price of the order is {order.total_cart_price}"})


#### RESERVATION ####

@views.route('/dashboard/new/reservation', methods=['POST', 'GET'], strict_slashes=False)
def new_reservation():
    """Creates a new reservation
    """
    name = request.form.get('name')
    description = request.form.get('description')
    duration = request.form.get('duration')
    start = request.form.get('start')
    end = request.form.get('end')
    nb_of_person = request.form.get('nb_of_person')
    additional_info = request.form.get('additional_info')
    tables = request.form.get('tables')
    category = request.form.get('category')
    try:
        reservation = RESERVATION.register_reservation(name, description, duration, start, end,
                                         nb_of_person, additional_info, tables, category)
    except ValueError:
        return make_response(jsonify({"message": "reservation already registered"}), 400)

    return jsonify({"reservation": reservation.name, 
                    "message": f"reservation {reservation.name} created"})