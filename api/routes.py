from flask import request, session, jsonify, render_template, redirect, url_for, abort
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError
import json
import bcrypt
from datetime import datetime

from app import app, db
# models
from api.db_models import Address, User, MenuItem, Menu, OrderItem, Order, \
PaymentMethod,\
Payment, TransactionItem, Transaction, ReservationItem, Reservation, \
Restaurant, ShipmentMethod, Shipment, Invoice, InvoiceItem, Event, EventItem,\
Information

@app.route('/')
def home():
    return render_template('home.html')

# AUTHENTICATION

@app.route('/auth/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    # if request.method == 'GET':
    #     return render_template('signup.html')

    # get user info from request
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    # generate salt and hash the password
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # create a new user object
    new_user = User(email=email,
                    password=password_hash,
                    first_name=first_name,
                    last_name=last_name,
                    created_at=datetime.utcnow())
    
    # try to add user to database
    try:
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already registered'})
    

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # get user info from request
    email = request.json.get('email')
    password = request.json.get('password')

    # query the user email and password
    user = db.session.query(User).filter_by(email=email).first()

    if user and bcrypt.checkpw(password, user.password.encode('utf-8')):
        session['user_id'] = user.id
        return redirect(url_for('home'))
    else:
        return jsonify({'error': 'Incorrect email or password'})

@app.route('/auth/logout', methods=['POST'], strict_slashes=False)
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))



# ADDRESS

@login_required
@app.route('/new/address', methods=['GET', 'POST'], strict_slashes=False)
def add_address():
    # get adddress info from request
    data = request.get_json()
    address_one = data.get('address_one')
    address_two = data.get('address_two')
    phone_number = data.get('phone_number')
    city = data.get('city')
    city_area = data.get('city_area')
    country = data.get('country')
    country_area = data.get('country_area')
    user = current_user

    new_address = Address(address_one=address_one,
                          address_two=address_two,
                          phone_number=phone_number,
                          city=city,
                          city_area=city_area,
                          country=country,
                          country_area=country_area,
                          user=user)
    
    db.session.add(new_address)
    db.session.commit()
    return jsonify({'Address added successfully'})

@login_required
@app.route('/account/address/<int: address_id>', methods=['GET'])
def address(address_id):
    # get the user address
    address = db.session.query(Address).get_or_404(address_id)
    if address.user != current_user:
        abort(403)

    return jsonify({
        "id": address.id,
        "first_name": address.first_name,
        "last_name": address.last_name,
        "address_one": address.address_one,
        "address_two": address.address_two,
        "phone_number": address.phone_number,
        "city": address.city,
        "city_area": address.city_area,
        "country": address.country,
        "country_area": address.country_area})

@login_required
@app.route('/account/address/<int: address_id>/update', methods=['GET', 'POST'])
def update_address(address_id):
    address = db.session.query(Address).get_or_404(address_id)
    if address.user != current_user:
        abort(403)
    
    data = request.get_json()
    address.address_one = data.get('address_one')
    address.address_two = data.get('address_two')
    address.phone_number = data.get('phone_number')
    address.city = data.get('city')
    address.city_area = data.get('city_area')
    address.country = data.get('country')
    address.country_area = data.get('country_area')
    
    db.session.commit()
    return jsonify({'Address updated successfully'})

@login_required
@app.route('/account/address/<int: address_id>/delete', methods=['POST'])
def delete_address(address_id):
    address = db.session.query(Address).get_or_404(address_id)
    if address.user != current_user:
        abort(403)

    db.session.delete(address)
    db.session.commit()
    return redirect(url_for('address'))



# RESTAURANT

@login_required
@app.route('/new/restaurant', methods=['GET', 'POST'], strict_slashes=False)
def add_restaurant():
    # get restaurant info from request
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    location = data.get('location')
    is_operational = data.get('is_operational')
    order_fulfilling = data.get('order_fulfilling')
    payment_methods = data.get('payment_methods')
    offers = data.get('offers')
    suppliers = data.get('suppliers')
    
    reservations = db.session.query(Reservation).filter_by(Restaurant.id).first()

    restaurant = Restaurant(name=name,
                            description=description,
                            location=location,
                            is_operational=is_operational,
                            order_fulfilling=order_fulfilling,
                            payment_methods=payment_methods,
                            offers=offers,
                            suppliers=suppliers,
                            reservations = reservations,
                            created_at=datetime.utcnow())
    
    db.session.add(restaurant)
    db.session.commit()
    return jsonify({'Restaurant created successfully'})


# MENU ITEM


@login_required
@app.route('/new/menu_item', methods=['GET', 'POST'], strict_slashes=False)
def add_menu_item():
    # get menu item info from request
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    category = data.get('category')
    price = data.get('price')
    foods = data.get('foods')
    is_available = data.get('is_available')
    is_delivrable = data.get('is_delivrable')
    duration_of_preparation = data.get('duration_of_preparation')

    menu = Menu(name=name,
                description=description,
                category=category,
                price=price,
                foods=foods,
                is_available=is_available,
                is_delivrable=is_delivrable,
                duration_of_preparation=duration_of_preparation,
                created_at=datetime.utcnow())
    
    db.session.add(menu)
    db.session.commit()
    return jsonify({'Menu item created successfully'})



# MENU


@login_required
@app.route('/new/menu', methods=['GET', 'POST'], strict_slashes=False)
def add_menu():
    # get menu info from request
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    category = data.get('category')
    items = data.get('items')

    menu = Menu(name=name,
                description=description,
                category=category,
                items=items,
                created_at=datetime.utcnow())
    
    db.session.add(menu)
    db.session.commit()
    return jsonify({'Menu created successfully'})

@app.route('/dashboard/menu/<int: menu_id>')
def menu(menu_id):
    menu = db.session.query(Menu).get_or_404(menu_id)
    return menu

@login_required
@app.route('/dashboard/menu/<int: menu_id>/update')
def update_menu(menu_id):
    menu = db.session.query(Menu).get_or_404(menu_id)


# ORDER

@login_required
@app.route('/new/order', methods=['GET', 'POST'], strict_slashes=False)
def add_order():
    # get menu info from request
    data = request.get_json()
    items = data.get('items')
    address = data.get('address')
    shipment_method = data.get('shipment_method')
    payment_method = data.get('payment_method')
    menu = Menu(items=items,
                address=address,
                shipment_method=shipment_method,
                payment_method=payment_method,
                created_at=datetime.utcnow())
    
    db.session.add(menu)
    db.session.commit()
    return jsonify({'Menu created successfully'})