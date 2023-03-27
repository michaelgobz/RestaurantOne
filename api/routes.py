import os
from datetime import datetime
from os.path import dirname, join
from re import A
from uuid import uuid4

import bcrypt
from dotenv import load_dotenv
from flask import Blueprint, abort, jsonify, redirect, request, url_for
from flask_jwt_extended import (create_access_token, get_jwt, get_jwt_identity,
                                jwt_required)
from jwt import decode, encode
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import contains_eager

# models
from api.db_models import (Address, Cart, CartItem, Menu, MenuItem, Order,
                           OrderItem, Payment, PaymentMethod, Reservation,
                           Restaurant, Shipment, Transaction, User,
                           VerificationToken)
from app import db

# load env variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# use blueprint to create a new routes
api = Blueprint('api', __name__, url_prefix='/api/v1/')

blacklist = set()


# initial route


@api.route('/')
def home():
    return jsonify({
        "message": "welcome to the Restaurant One",
        "company": "RestaurantOne",
        "location": "Africa",
        "year": 2023,
        "month": "March",
        "Version": "1.0.0",
        "Project": "Alx-webstack project",
        "supervisor": "Alx-SE Mentors",
        "api-prefix": "api/v1",
        "authors": "@michaelGoboola and @jedBahena"
    })


# ------------------------------------- AUTHENTICATION ------------------------------------- #


@api.route('/auth/signup', methods=['POST'], strict_slashes=False)
def signup():
    """Sign up a new user"""
    # get user info from request
    data = request.get_json()

    password = data.get('password')

    # generate salt and hash the password
    salt = bcrypt.gensalt(rounds=12, prefix=b'2b')
    salt_to_string = salt.decode('utf-8')
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

    # create a new user object
    new_user = User(id=str(uuid4()),
                    email=data.get('email'),
                    password=password_hash.decode('utf-8'),
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    role=data.get('role'),
                    salt=salt_to_string,
                    phone_number=data.get('phonenumber'),
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow())

    # try to add user to database
    try:
        db.get_session().add(new_user)

        # generate verification token
        new_user_created = db.get_session().query(User). \
            filter_by(email=data.get('email')).first()
        token = encode({'email': new_user_created.email},
                       os.environ.get('SECRET_KEY'), algorithm="HS256")
        # send verification email

        # store the verification token in the database
        user_verification_token = VerificationToken(id=str(uuid4()),
                                                    token=token,
                                                    created_at=datetime.utcnow(),
                                                    user_id=new_user.id)
        db.get_session().add(user_verification_token)
        db.get_session().commit()
        return jsonify({'message': 'user created successfully',
                        'redirect': 'login',
                        'details': 'check your email to confirm your account',
                        'token': token})
    except IntegrityError:
        db.get_session().rollback()
        return jsonify({'error':
                            'Email already registered  or server error or token error'})


@api.route('/auth/login', methods=['POST'], strict_slashes=False)
def login():
    # get user info from request
    email = request.json.get('email')
    password = request.json.get('password')

    # query the user email and password
    user = db.get_session().query(User).filter_by(email=email).first()
    # hash the password and compare with the password in the database
    salt = user.salt
    user_password = user.password
    # b = bytes(user_password,'utf-8')
    hashed_password = bcrypt.hashpw(password.encode(
        'utf-8'), bytes(salt, 'utf-8'))

    if user and user_password == hashed_password.decode('utf-8'):
        # generate a JWT token with user ID as the identity
        access_token = create_access_token(identity=user.id)

        # send the token back to the client
        return jsonify({'access_token': access_token,
                        'message': 'Successfully logged in',
                        'user_id': user.id})
    else:
        return jsonify({'error': 'Incorrect email or password'}), 401


@api.route('/auth/logout', methods=['POST'], strict_slashes=False)
@jwt_required()  # uth headers should be set with the correct token
def logout():
    # Blacklist the current access token so that it can no longer be used
    jti = get_jwt()['jti']
    blacklist.add(jti)

    # Return a response indicating success
    return jsonify({'message': 'Successfully logged out'}), 200


@api.route('/auth/reset_password', methods=['POST'], strict_slashes=False)
def reset_password():
    """Reset password for a user
    Returns:
        _type_: token
    """
    email = request.json.get('email')
    user = db.get_session().query(User).filter_by(email=email).first()
    # check for the email in the database
    if email is None:
        return jsonify({'error': 'Email is required'})
    elif user is None:
        return jsonify({'error': 'Email does not exist'})
    elif user.email == email:
        secret = os.environ.get('SECRET_KEY')
        # generate token and send to the user email
        token = encode({'set_password': 'true', 'user_id': user.id},
                       secret, algorithm="HS256")
        # store the password reset token in the database
        user.password_reset_token = token
        db.get_session().commit()
        return jsonify({'message': 'token is sent to your email',
                        'token': token
                        })


@api.route('/auth/reset_password/<token>', methods=['POST'], strict_slashes=False)
def set_password(token):
    payload = decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
    user_id = payload['user_id']
    user = db.get_session().query(User).filter_by(id=user_id).first()
    password = request.json.get('password')
    # generate salt and hash the password
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    user.password = password_hash
    db.get_session().commit()

    return jsonify({'message': 'password reset successful',
                    'details': 'login to continue'})


@api.route('/auth/confirm_account/<token>', methods=['GET'], strict_slashes=False)
def confirm_account(token):
    """Confirm user account
    Returns:
        _type_: message
    """
    payload = decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
    email = payload['email']
    user = db.get_session().query(User).filter_by(email=email).first()
    if user:
        user.is_verified = True
        db.get_session().commit()
        return jsonify({'message': 'Account confirmed successfully',
                        'redirect': 'login',
                        'details': 'welcome to the Restaurant One'})
    else:
        return jsonify({'error': 'Account not found'})


@api.route('/admin/verification/<user_id>', methods=['GET'], strict_slashes=False)
@jwt_required()  # needs jwt token based authentication in the authorization header
def verification(user_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)

    if user.role != 'admin':
        return abort(403)

    customer_id = user_id

    customer = db.get_session().query(User).get_or_404(customer_id)

    customer = User(verified=True)
    db.get_session().commit()
    return jsonify({'message': 'Admin has been Verified'})


# ------------------------------------- DASHBOARDS ------------------------------------- #


# admin dashboard
@api.route('/admin/dashboard/<int:user_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def admin_dashboard(user_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)

    # admin dashboard
    if user.role == 'admin':
        return abort(403)

    restaurants = db.get_session().query(Restaurant).all()
    if not restaurants:
        return jsonify({'message': 'No restaurant to display'}), 404
    # return the restaurant object as a JSON response
    return jsonify([restaurant.serialize() for restaurant in restaurants]), 200


# manager dashboard
@api.route('/manager/dashboard/<int:user_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def manager_dashboard(user_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)
    # manager dashboard
    if user.role != 'manager':
        return abort(403)

    restaurants = db.get_session().query(Restaurant).filter(
        Restaurant.manager_id == current_user).all()
    if restaurants:
        # Initialize an empty dictionary to store the serialized Menu objects for each Restaurant.
        all_menus = {}
        for restaurant in restaurants:
            menus = db.get_session().query(Menu).filter(
                Menu.restaurant_id == restaurant.id).all()
            # If there are no Menu objects for the current Restaurant,add an empty list of menus to the all_menus dictionary.
            if not menus:
                all_menus[restaurant.id] = {
                    'restaurant_name': restaurant.name, 'menus': []}
            else:
                # If there are Menu objects for the current Restaurant, add a list of serialized menus to the all_menus dictionary.
                all_menus[restaurant.id] = {'restaurant_name': restaurant.name, 'menus': [
                    menu.serialize() for menu in menus]}

        # Serialize the all_menus dictionary as JSON and return it as the response.
        return jsonify(all_menus), 200

    return jsonify({'message': 'No restaurant to display'}), 404


# ------------------------------------- USER PROFILE ------------------------------------- #


# get profile
@api.route('/me/account/profile/<user_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def profile(user_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get the user profile information form DB
    user_profile = db.get_session().query(User).get_or_404(current_user)
    if not profile:
        return jsonify({'error': 'No profile found'}), 404
    # return a list of user objects as a JSON response
    return jsonify([element.serialize() for element in user_profile]), 200


# update profile


@api.route('/me/account/update_profile/<user_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_profile():
    # access the identity of the current user
    current_user = get_jwt_identity()
    # get the user profile information from the DB
    current_user_profile = db.get_session().query(User).get_or_404(current_user)

    # Update profile
    data = request.get_json()

    if 'email' in data:
        current_user_profile.email = data['email']
    if 'first_name' in data:
        current_user_profile.first_name = data['first_name']
    if 'last_name' in data:
        current_user_profile.last_name = data['last_name']
    if 'addresses' in data:
        current_user_profile.addresses = data['addresses']

    current_user_profile.updated_at = datetime.utcnow()

    # Commit changes to DB
    db.get_session().commit()
    new_user_profile = db.get_session().query(User).get_or_404(current_user)

    return jsonify({'message': 'Profile updated successfully',
                    'new_profile': [element.serialize() for element in new_user_profile]})


# ------------------------------------- ADDRESS ------------------------------------- #


@api.route('/account/address/new/<user_id>', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_address(user_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get address info from request
    data = request.get_json()

    # create a new address object and add it to the database
    new_address = Address(id=str(uuid4()),
                          address_one=data.get('address_one'),
                          address_two=data.get('address_two'),
                          phone_number=data.get('phone_number'),
                          city=data.get('city'),
                          city_area=data.get('city_area'),
                          country=data.get('country'),
                          country_area=data.get('country_area'),
                          user_id=current_user)
    db.session.add(new_address)
    db.session.commit()

    # return a success response
    return jsonify({'message': 'Address added successfully',
                    'new_address': [element.serialize() for element in new_address]}), 200


# get addresses


@api.route('/account/addresses/<user_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_addresses(user_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # retrieve all addresses for the user from the database
    addresses = db.get_session().query(Address).filter_by(user_id=current_user).all()
    # return a list of address objects as a JSON response
    return jsonify({'Addresses': [address.serialize() for address in addresses]}), 200


# get an address


@api.route('/account/address/<address_id>/<user_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_address(user_id, address_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # retrieve the specific address for the user from the database
    address = db.get_session().query(Address).filter_by(
        id=address_id, user_id=current_user).first()
    if not address:
        return jsonify({'error': 'Address not found'}), 404
    # return the address object as a JSON response
    return jsonify({'chosen_address': [element.serialize() for element in address]}), 200


# update address


@api.route('/account/address/<address_id>/<user_id>',
           methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_address(user_id, address_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # retrieve the address to update from the database
    address = db.get_session().query(Address).filter_by(
        id=address_id, user_id=current_user).first()
    if not address:
        return jsonify({'error': 'No address found',
                        'message': 'Address Missing the Update was not successfully'}), 404

    # Update the address
    data = request.get_json()

    if 'address_one' in data:
        address.address_one = data['address_one']
    if 'address_two' in data:
        address.address_two = data['address_two']
    if 'phone_number' in data:
        address.phone_number = data['phone_number']
    if 'city' in data:
        address.city = data['city']
    if 'city_area' in data:
        address.city_area = data['city_area']
    if 'country' in data:
        address.country = data['country']
    if 'country_area' in data:
        address.country_area = data['country_area']

    # Commit changes to DB
    db.get_session.commit()
    new_updated_address = db.get_session().query(Address).filter_by(
        id=address_id, user_id=current_user).first()
    db.get_session().commit()
    return jsonify({'message': 'Address updated successfully',
                    'updated_address': [element.serialize() for element in new_updated_address]}), 200


# delete address


@api.route('/account/address/delete/<user_id>/<address_id>',
           methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_address(user_id, address_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # retrieve the address to update from the database
    address = db.get_session.query(Address).filter_by(
        id=address_id, user_id=current_user).first()
    if not address:
        return jsonify({'error': 'Address not found'}), 404

    # delete the address data in the db
    db.get_session().delete(address)
    db.get_session().commit()
    return jsonify({
        'message': 'Delete Successfully',
        'address_id': address_id,
        'details': 'address with the id you supplied has been deleted'
    })


# ------------------------------------- RESTAURANT ------------------------------------- #


# Create restaurant
@api.route('/account/restaurant/new/<user_id>',
           methods=['POST'], strict_slashes=False)
@jwt_required()
def add_restaurant(user_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)
    # check if user is manager
    if user.role != 'admin':
        abort(403)
    # Get restaurant info from request
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')
    location = data.get('location')
    is_operational = data.get('isOperational')
    order_fulfilling = data.get('isOrderFulfilling')
    offers = data.get('offers')
    suppliers = data.get('suppliers')
    avatar = data.get('avatar')
    customers = data.get('customers')

    # Validate input data
    if not name or not location:
        return jsonify({'error': 'Name and location are required'}), 400
    if not isinstance(is_operational, bool):
        return jsonify({'error': 'is_operational must be a boolean'}), 400

    # Create a new restaurant object
    restaurant = Restaurant(
        id=str(uuid4()),
        name=name,
        description=description,
        location=location,
        is_operational=is_operational,
        order_fulfilling=order_fulfilling,
        avatar=avatar,
        offers=offers,
        customers=customers,
        suppliers=suppliers,
        manager_id=current_user,
        created_at=datetime.utcnow()
    )

    # Add the new restaurant object to the session and commit the changes
    db.get_session().add(restaurant)
    db.get_session().commit()

    # Return a JSON response with the ID of the newly created restaurant
    return jsonify({'message': 'Restaurant created successfully',
                    'restaurant_id': restaurant.id}), 200


# simple get all restaurants

@api.route('/dashboard/restaurants', methods=['GET'], strict_slashes=False)
def get_restaurants():
    """Get all restaurants"""
    restaurants = db.get_session().query(Restaurant).all()
    db.get_session().commit()
    return jsonify({'message': ' restaurants returned successfully',
                    'restaurants': [restaurant.serialize for restaurant in restaurants]})

# simple get restaurant by id


@api.route('/dashboard/restaurants/<restaurant_id>', methods=['GET'],
           strict_slashes=False)
def get_restaurant_by_id(restaurant_id):
    """Get a restaurant by id"""
    restaurant = db.get_session().query(Restaurant).get_or_404(restaurant_id)
    db.get_session().commit()
    return jsonify({'message': ' restaurant returned successfully',
                    'restaurant': restaurant.serialize})



# Update restaurant
@api.route('/account/restaurant/update/<user_id>/<restaurant_id>',
           methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_restaurant(user_id, restaurant_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)
    # check if user is admin
    if (user.role != 'admin' or user.role != 'manager'):
        abort(403)

    # get the restaurant from the DB
    restaurant = db.get_session().query(Restaurant).get_or_404(restaurant_id)

    # Update restaurant
    data = request.get_json()

    if 'name' in data:
        restaurant.name = data['name']
    if 'description' in data:
        restaurant.description = data['description']
    if 'location' in data:
        restaurant.location = data['location']
    if 'is_operational' in data:
        restaurant.is_operational = data['is_operational']
    if 'order_fulfilling' in data:
        restaurant.order_fulfilling = data['order_fulfilling']
    if 'payment_methods' in data:
        restaurant.payment_methods = data['payment_methods']
    if 'offers' in data:
        restaurant.offers = data['offers']
    if 'suppliers' in data:
        restaurant.suppliers = data['suppliers']

    restaurant.updated_at = datetime.utcnow()

    # Commit the updated data to the database
    db.get_session().commit()
    return jsonify({'message': 'Restaurant updated successfully'}), 200


# delete a restaurant
@api.route('/dashboard/restaurant/delete/<user_id>/<restaurant_id>',
           methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_restaurant(user_id, restaurant_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)

    # check whether the user is admin, manager or simple user
    if user.role == 'admin':
        abort(403)

    # get the restaurant from the DB
    restaurant = db.get_session().query(Restaurant).get_or_404(restaurant_id)

    # delete the restaurant from the DB
    db.get_session().delete(restaurant)
    db.get_session().commit()

    return jsonify({'message': 'Restaurant deleted successfully'}), 200


# ------------------------------------- MENU ------------------------------------- #


# Create Menu
"""Create a new menu for a restaurant"""


@api.route('/account/restaurant/menu/new/<user_id>/<restaurant_id>',
           methods=['POST'], strict_slashes=False)
@jwt_required()
def add_menu(user_id, restaurant_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)
    # check if user is admin
    if user.role != 'admin':
        abort(403)

    # Retrieve the restaurant by id
    restaurant = db.get_session().query(
        Restaurant).filter_by(id=restaurant_id).first()
    if not restaurant:
        return jsonify({'error': 'No restaurant found'}), 404

    # Get menu info from request
    data = request.get_json()

    # Create a new menu object
    menu = Menu(
        id=str(uuid4()),
        restaurant_id=restaurant_id,
        name=data.get('name'),
        description=data.get('description'),
        category=data.get('category'),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    # Add the new menu object to the session and commit
    db.get_session().add(menu)
    db.get_session().commit()

    # Return a JSON response
    return jsonify({'message': 'Menu created successfully',
                    'menu_id': menu.id
                    }), 200


# get menus


"""Get all menus available"""


@api.route('/dashboard/menus/', methods=['GET'], strict_slashes=False)
def get_menus():
    # retrieve all menus from the database
    menus = db.get_session().query(Menu).all()
    # return a list of menu objects as a JSON response
    return jsonify({'message': 'menus retrieved successfully',
                    'menus': [menu.serialize for menu in menus]}), 200


# get a menu


@api.route('/dashboard/menu/<menu_id>', methods=['GET'], strict_slashes=False)
def get_menu(menu_id):
    # retrieve the specific menu for the user from the database
    menu = db.get_session().query(Menu).filter_by(id=menu_id).first()
    if not menu:
        return jsonify({'error': 'No menu found'}), 404
    # return a list of menu object as a JSON response
    return jsonify([element.serialize for element in menu]), 200


# Update menu

@api.route('/account/restaurant/menu/update/<user_id>/<int:restaurant_id>/<menu_id>',
           methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_menu(user_id, restaurant_id, menu_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)
    # check if user is admin
    if user.role != 'admin' or user.role != 'manager':
        abort(403)

    # Retrieve the restaurant by id
    restaurant = db.get_session().query(
        Restaurant).filter_by(id=restaurant_id).first()
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    # Get the menu to update
    menu = db.get_session().query(Menu).get_or_404(menu_id)

    # Get updated menu info from request
    data = request.get_json()

    # Update the menu object
    if 'name' in data:
        menu.name = data['name']
    if 'description' in data:
        menu.description = data['description']
    if 'category' in data:
        menu.category = data['category']
    if 'price' in data:
        menu.price = data['price']
    if 'is_available' in data:
        menu.is_available = data['is_available']
    if 'is_deliverable' in data:
        menu.is_deliverable = data['is_deliverable']

    # Commit changes to DB

    db.get_session().add(menu)
    db.get_session().commit()

    # Return a JSON response
    return jsonify({'message': 'Menu updated successfully',
                    'menu_id': menu.id}), 200


"""Delete a menu"""


@api.route('/account/restaurant/menu/delete/<user_id>/<restaurant_id>/<menu_id>',
           methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_menu(user_id, restaurant_id, menu_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)
    # check if user is admin
    if user.role != 'admin' or user.role != 'manager':
        abort(403)

    # Retrieve the restaurant by id
    restaurant = db.get_session().query(
        Restaurant).filter_by(id=restaurant_id).first()
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    # get menu from the DB
    menu = db.get_session().query(Menu).get_or_404(menu_id)

    # delete the menu
    db.get_session().delete(menu)
    db.get_session().commit()

    return jsonify({'message': 'Menu deleted successfully',
                    'menu_id': menu.id,
                    'details': 'menu with id you supplied is deleted'}), 200


# ------------------------------------- MENU ITEM ------------------------------------- #

"""Create a new menu item"""

"""get all menu items"""


@api.route('/dashboard/menu/menu_items/', methods=['GET'], strict_slashes=False)
def get_menu_items():
    menu_items = db.get_session().query(MenuItem).all()
    print(type(menu_items[0]))
    return jsonify({'message': 'Menu items retrieved successfully',
                    'menu_items': [menu_item.serialize
                                   for menu_item in menu_items]}), 200


# Create menu item


@api.route('/account/menu/menu_item/new/<user_id>/<menu_id>',
           methods=['POST'], strict_slashes=False)
@jwt_required()
def add_menu_item(user_id, menu_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)
    # check if user is admin
    if user.role != 'admin':
        abort(403)

    # Retrieve the menu by id
    menu = db.get_session().query(Menu).filter_by(id=menu_id).first()
    if not menu:
        return jsonify({'error': 'Menu not found!'}), 404
    # Get menu item info from request
    data = request.get_json()

    menu_item = MenuItem(
        id=str(uuid4()),
        menu_id=menu_id,
        name=data.get('name'),
        description=data.get('description'),
        foods=data.get('foods'),
        category=menu.category,
        is_available=data.get('isAvailable'),
        is_deliverable=data.get('isDeliverable'),
        price=data.get('price'),
        duration_of_preparation=data.get('durationOfPreparation'),
        rating=data.get('rating'),
        avatar=data.get('avatar'),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    # Add the new menu object to the session and commit the changes
    db.get_session().add(menu_item)
    db.get_session().commit()

    # Return a JSON response
    return jsonify({'message': 'Menu item created successfully',
                    'menu_item_id': menu_item.id}), 200


# get menu items

# Read menu item
@api.route('/dashboard/menu_item/<item_id>',
           methods=['GET'], strict_slashes=False)
def menu_item(item_id):
    # get the menu_item from the DB
    menu_item = db.get_session().query(MenuItem).get_or_404(item_id)

    # return a list of menu object as a JSON response
    return jsonify({'elements': menu_item.serialize,
                    'status': 'Successfully'}), 200


# Update menu item
@api.route('/account/menu/update/menu_item/<user_id>/<menu_id>/<item_id>',
           methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_menu_item(user_id, menu_id, item_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)
    # check if user is admin
    if user.role != 'admin' or user.role != 'manager':
        abort(403)

    # Retrieve the menu by id
    menu = db.get_session().query(Menu).filter_by(id=menu_id).first()
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404

    # get the menu_item information from the DB
    menu_item = db.get_session().query(MenuItem).get_or_404(item_id)

    # get the menu_item info from the user and update them in the db
    data = request.get_json()

    # Update the menu item object
    if 'name' in data:
        menu_item.name = data['name']
    if 'description' in data:
        menu_item.description = data['description']
    if 'category' in data:
        menu_item.category = data['category']
    if 'foods' in data:
        menu_item.foods = data['foods']
    if 'duration_of_preparation' in data:
        menu_item.duration_of_preparation = data['duration_of_preparation']

    menu_item.updated_at = datetime.utcnow()

    # Commit the changes to DB
    db.get_session().commit()
    return jsonify({'message': 'Menu item updated successfully',
                    'menu_item_id': menu_item.id}), 200


# Delete menu item
@api.route('/account/menu/menu_item/delete/<user_id>/<menu_id>/<item_id>',
           methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_menu_item(user_id, menu_id, item_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # get user from the DB
    user = db.get_session().query(User).get_or_404(current_user)
    # check if user is admin
    if user.role != 'admin' or user.role != 'manager':
        abort(403)
    # Retrieve the menu by id
    menu = db.get_session().query(Menu).filter_by(id=menu_id).first()
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404
    # get the menu item from the DB
    menu_item = db.get_session().query(MenuItem).get_or_404(item_id)

    # delete the menu item
    db.get_session().delete(menu_item)
    db.get_session().commit()

    return jsonify({'message': 'Menu item deleted successfully'}), 200


# ------------------------------------- CART ------------------------------------- #


# add an item to cart
@api.route('/dashboard/<int:user_id>/cart/add', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_item_to_cart(user_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # Parse the data from the request
    data = request.get_json()
    menu_id = data.get('menu_id')
    quantity = data.get("quantity")

    # retrieve the menu from the DB
    menu = db.get_session().query(Menu).filter_by(id=menu_id).first()

    if not menu:
        return jsonify({'message': 'Menu not found!'}), 404
    if not quantity or quantity < 1:
        return jsonify({'error': 'Invalid quantity'}), 400

    # retrieve the user's cart from the DB
    cart = db.get_session().query(Cart).filter_by(user_id=current_user).first()

    # if the user doesn't have a cart, create a cart
    if not cart:
        cart = Cart(
            id=str(uuid4()),
            user_id=current_user,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.get_session().add(cart)
        db.get_session().commit()

        # retrieve the user's cart from the DB after its creation
        cart = db.get_session().query(Cart).filter_by(user_id=current_user).first()

    # check if the menu is already in the cart
    cart_item = db.get_session().query(CartItem).filter_by(
        cart_id=cart.id, menu_id=menu_id).first()

    # if the menu is already in the cart, add the quantity
    if cart_item:
        cart_item.quantity += quantity
    else:
        # set a default price for the item if it's not already in the cart
        price = menu.price if menu else 0.0

    # add the menu to the cart
    cart_item = CartItem(
        id=str(uuid4()),
        cart_id=cart.id,
        menu_id=menu_id,
        quantity=quantity,
        price=price
    )

    db.get_session().add(cart_item)
    db.get_session().commit()

    return jsonify({'message': 'Item added to cart successfully!'}), 201


# ------------------------------------- ORDER ------------------------------------- #


@api.route('/account/order/add/<user_id>', methods=['POST'], strict_slashes=False)
@jwt_required()
def place_order(user_id):
    # Access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)

    # Parse the data from the request
    data = request.get_json()

    # Get the cart for the current user
    cart = db.get_session().query(Cart).filter_by(user_id=current_user).first()

    # Check if the cart is empty
    if not cart.items:
        return jsonify({'message': 'Your cart is empty!'}), 400

    # Create a new order for the current user
    order = Order(
        id=str(uuid4()),
        user_id=current_user,
        restaurant_id=cart.items[0].menu_item.menu.restaurant.id,
        address=data.get('address'),
        shipment_method=data.get('shipment_method'),
        payment_method=data.get('payment_method'),
        notes=data.get('notes'),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    # Add the items from the cart to the order
    for item in cart.items:
        order_item = OrderItem(id=str(uuid4()),
                               menu_id=item.menu_id,
                               quantity=item.quantity,
                               price=item.price)

        db.get_session().add(order_item)
        db.get_session().commit()

    # total price of the order
    total_price = sum([item.menu.price * item.quantity for item in cart.items])
    order.total_price = total_price
    order.status = 'succeeded'

    # Clear the cart
    for item in cart.items:
        db.get_session().delete(item)

    db.get_session().commit()

    # Add the order to the DB
    db.get_session().add(order)
    db.get_session().commit()

    return jsonify({'message': 'Order placed successfully!',
                    'order_id': order.id}), 201


# get orders
@api.route('/account/orders/<user_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_orders(user_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # retrieve all orders for the user from the database
    orders = db.get_session().query(Order).filter_by(user_id=current_user).all()
    # return a list of order objects as a JSON response
    return jsonify({'orders': [order.serialize() for order in orders]}), 200


# get an order


@api.route('/account/order/<user_id>/<order_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_order(user_id, order_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # retrieve the specific order for the user from the database
    order = db.get_session().query(Order).filter_by(
        id=order_id, user_id=current_user).first()
    if not order:
        return jsonify({'error': 'Order not found!'}), 404
    # return the order object as a JSON response
    return jsonify({'elements': [element.serialize() for element in order]}), 200


# Delete order
@api.route('/dashboard/<int:user_id>/order/<int:order_id>/delete', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_order(user_id, order_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # Get the order from the DB
    order = db.get_session().query(Order).filter_by(
        id=order_id, user_id=current_user).first()
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    # Remove the order from the DB

    db.get_session().delete(order)
    db.get_session().commit()

    # Return a success message to the user
    return jsonify({'message': 'Order deleted successfully!'})


# ------------------------------------- RESERVATION ------------------------------------- #


# add reservation
@api.route('/dashboard/restaurant/reservation/add/<user_id>/<restaurant_id>',
           methods=['POST'], strict_slashes=False)
@jwt_required()
def add_reservation(user_id, restaurant_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # Parse the data from the request
    data = request.get_json()
    # get the restaurant of the reservation
    restaurant = db.get_session().query(Restaurant).get_or_404(restaurant_id)
    # Create a new reservation object
    reservation = Reservation(
        id=str(uuid4()),
        user_id=current_user,
        restaurant_id=restaurant.id,
        description=data.get('description'),
        duration=data.get('duration'),
        start=data.get('start'),
        end=data.get('end'),
        nb_of_person=data.get('nb_of_person'),
        menu_id=data.get('menu_id'),
        additional_info=data.get('additional_info'),
        tables=data.get('tables'),
        price=data.get('price'),
        tax=data.get('tax'),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    # Add the reservation to the DB
    db.get_session().add(reservation)
    db.get_session().commit()

    # Return a success message to the user
    return jsonify({'message': 'Reservation added successfully!'}), 201


# get reservations
@api.route('/customer/reservations/<user_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_reservations(user_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # retrieve all reservations for the user from the database
    reservations = db.get_session().query(
        Reservation).filter_by(user_id=current_user).all()
    # return a list of reservation objects as a JSON response
    return jsonify([reservation.serialize() for reservation in reservations]), 200


# get a reservation


@api.route('/customer/reservation/<user_id>/<reservation_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_reservation(user_id, reservation_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # retrieve the specific reservation for the user from the database
    reservation = db.get_session().query(Reservation).filter_by(
        id=reservation_id, user_id=current_user).first()
    if not reservation:
        return jsonify({'error': 'reservation not found!'}), 404
    # return the reservation object as a JSON response
    return jsonify([element.serialize() for element in reservation]), 200


# Update reservation


@api.route('/dashboard/reservation/update/<user_id>/<reservation_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_reservation(user_id, reservation_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # retrieve the reservation to update from the database
    reservation = db.get_session().query(Reservation).filter_by(
        id=reservation_id, user_id=current_user).first()
    if not reservation:
        return jsonify({'error': 'No reservation found'}), 404
    # Parse the data from the request
    data = request.get_json()

    # Update the reservation object
    if 'description' in data:
        reservation.description = data['description']
    if 'duration' in data:
        reservation.duration = data['duration']
    if 'start' in data:
        reservation.start = data['start']
    if 'end' in data:
        reservation.end = data['end']
    if 'nb_of_person' in data:
        reservation.nb_of_person = data['nb_of_person']
    if 'additional_info' in data:
        reservation.additional_info = data['additional_info']
    if 'tables' in data:
        reservation.tables = data['tables']
    if 'category' in data:
        reservation.category = data['category']
    if 'price' in data:
        reservation.price = data['price']
    if 'tax' in data:
        reservation.tax = data['tax']
    if 'menu_id' in data:
        reservation.menu_id = data['menu_id']

    reservation.updated_at = datetime.utcnow()

    # Commit the changes to the DB
    db.get_session().commit()

    # Return a success message to the user
    return jsonify({'message': 'Reservation updated successfully!'}), 200


"""delete reservation"""


# Delete reservation


@api.route('/dashboard/reservation/delete/<user_id>/<reservation_id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_reservation(user_id, reservation_id):
    # access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)
    # Get the reservation from the DB
    reservation = db.get_session().query(Reservation).filter_by(
        id=reservation_id, user_id=current_user).first()
    if not reservation:
        return jsonify({'error': 'Reservation not found'}), 404

    # Remove the reservation from the DB

    db.get_session().delete(reservation)
    db.get_session().commit()

    # Return a success message to the user
    return jsonify({'message': 'Reservation deleted successfully!'}), 200


# ------------------------------------- CHECKOUT ------------------------------------- #


@api.route('/customer/order/checkout/<user_id>/<order_id>', methods=['POST'], strict_slashes=False)
@jwt_required()
def checkout(user_id, order_id):
    # Access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)

    # Parse the data from the request
    data = request.get_json()

    order = db.get_session().query(Order).filter_by(id=order_id).first()
    if not order:
        return jsonify({'message': 'No order found'}), 404

    payment_method = db.get_session().query(
        PaymentMethod).filter_by(user_id=current_user).first()
    if not payment_method:
        payment_method = PaymentMethod(
            id=str(uuid4()),
            user_id=current_user,
            type=data.get('type'),
            last4=data.get('last4'),
            exp_month=data.get('exp_month'),
            exp_year=data.get('exp_year'),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        db.get_session().add(payment_method)
        db.get_session().commit()
        payment_method = db.get_session().query(
            PaymentMethod).filter_by(user_id=current_user).first()

    payment = Payment(
        id=str(uuid4()),
        order_id=order_id,
        payment_method_id=payment_method.id,
        amount=order.total_price,
        currency=data.get('currency'),
        status=data.get('status'),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    db.get_session().add(payment)
    db.get_session().commit()

    return jsonify({'message': 'Checkout proceeded successfully',
                    'checkout_id': payment.id}), 200


# ------------------------------------- TRANSACTION ------------------------------------- #


@api.route('/account/<user_id>/<order_id>', methods=['POST'], strict_slashes=False)
@jwt_required()
def transaction(user_id, order_id):
    # Access the identity of the current user
    current_user = get_jwt_identity()
    # check if the user ID from the JWT token matches the requested user ID
    if current_user != user_id:
        return abort(401)

    order = db.get_session().query(Order).get_or_404(order_id)

    data = request.get_json()

    payment = db.get_session().query(
        Payment).filter_by(order_id=order.id).first()

    transaction = Transaction(
        id=str(uuid4()),
        payment_id=payment.id,
        amount=payment.amount,
        currency=payment.currency,
        type=data.get('type'),
        status=data.get('status'),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.get_session().add(transaction)
    db.get_session().commit()

    return jsonify({'message': 'Transaction added successfully!',
                    'transaction_id': transaction.id}), 200
