
from re import A
from flask import request, session, jsonify, Blueprint, redirect, url_for, abort
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError
import json
import bcrypt
from datetime import datetime
from app import db
# models
from api.db_models import Address, User, MenuItem, Menu, Order, \
    Reservation, \
    Restaurant, Shipment


# use blueprint to create a new routes
api = Blueprint('api', __name__, url_prefix='/api/v1/')


# initial route

@api.route('/')
def home():
    return jsonify({
        "message": "welcome to the Our Platform",
        "company": "RestaurantOne",
        "location": "Kampala",
        "year": 2023,
        "month": "March",
        "Country": "Uganda",
        "Project": "Alx-webstack project",
        "supervisor": "Alx-SE Mentors",
        })
# ------------------------------------- AUTHENTICATION ------------------------------------- #

@api.route('/auth/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    # get user info from request
    data = request.get_json()

    password = data.get('password')
    # generate salt and hash the password
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # create a new user object
    new_user = User(email=data.get('email'),
                    password=password_hash,
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    created_at=datetime.utcnow())
    
    # try to add user to database
    try:
        db.get_session().add(new_user)
        db.get_session().commit()
        return redirect(url_for('login'))
    except IntegrityError:
        db.get_session().rollback()
        return jsonify({'error': 'Email already registered'})
    

@api.route('/auth/login', methods=['GET', 'POST'])
def login():
    # get user info from request
    email = request.json.get('email')
    password = request.json.get('password')

    # query the user email and password

    user = db.get_session().query(User).filter_by(email=email).first()

    if user and bcrypt.checkpw(password, user.password.encode('utf-8')):
        session['user_id'] = user.id
        return redirect(url_for('home'))
    else:
        return jsonify({'error': 'Incorrect email or password'})


@api.route('/auth/logout', methods=['POST'], strict_slashes=False)
def logout():
    # deletes the user session
    session.pop('user_id', None)
    return redirect(url_for('login'))

# ------------------------------------- USER PROFILE ------------------------------------- #

@login_required
@api.route('/me/account/profile/<int:user_id>', methods=['GET'], strict_slashes=False)
def profile(user_id):
    # get the user profile information form DB
    profile = db.get_session().query(User).get_or_404(user_id)
    if profile.user != current_user:
        abort(403)

    # return those data to the user
    return jsonify({
        "email": profile.email,
        "first_name": profile.first_name,
        "last_name": profile.last_name,
        "addresses": profile.addresses})

@login_required
@api.route('/me/account/<int:user_id>/update_profile', methods=['PUT'], strict_slashes=False)
def update_profile(user_id):
    """Update user profile

    Args:
        user_id (UUID): user id

    Returns:
        _type_: JSON
    """
    # get the user profile information from the DB
    profile = db.get_session().query(User).get_or_404(user_id)
    if profile.user != current_user:
        abort(403)

    # Update profile
    data = request.get_json()

    if 'email' in data:
        profile.email = data['email']
    if 'first_name' in data:
        profile.first_name = data['first_name']
    if 'last_name' in data:
        profile.last_name = data['last_name']
    if 'addresses' in data:
        profile.addresses = data['addresses']

    profile.updated_at=datetime.utcnow()

    # Commit changes to DB
    db.get_session().commit()

    return jsonify({'Profile updated successfully'})


# ------------------------------------- ADDRESS ------------------------------------- #

@login_required
@api.route('/account/<int:user_id>/address/new', methods=['POST'], strict_slashes=False)
def add_address(user_id):
    # get the user address from the DB
    address = db.get_session().query(Address).get_or_404(user_id)
    if address.user != current_user:
        abort(403)

    # get adddress info from request
    data = request.get_json()

    new_address = Address(address_one=data.get('address_one'),
                          address_two=data.get('address_two'),
                          phone_number=data.get('phone_number'),
                          city=data.get('city'),
                          city_area=data.get('city_area'),
                          country=data.get('country'),
                          country_area=data.get('country_area')
                          )
    
    db.get_session().add(new_address)
    db.get_session().commit()
    return jsonify({'Address added successfully'})

@login_required
@api.route('/account/<int:user_id>/address/', methods=['GET'])
def address(user_id):
    # get the user address from the DB
    address = db.get_session().query(Address).get_or_404(user_id)
    if address.user != current_user:
        abort(403)

    # Return them to the user
    return jsonify({
        "address_one": address.address_one,
        "address_two": address.address_two,
        "phone_number": address.phone_number,
        "city": address.city,
        "city_area": address.city_area,
        "country": address.country,
        "country_area": address.country_area})

@login_required
@api.route('/account/<int:user_id>/address/update', methods=['GET', 'POST'])
def update_address(user_id):
    # get the user address informations from the DB
    address = db.get_session().query(Address).get_or_404(user_id)
    if address.user != current_user:
        abort(403)
    
    # Update address
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
    return jsonify({'Address updated successfully'})

@login_required
@api.route('/account/<int:user_id>/address/delete', methods=['POST'])
def delete_address(user_id):
    # get the user address informations from the DB
    address = db.get_session().query(Address).get_or_404(user_id)
    if address.user != current_user:
        abort(403)

    # delete the address data in the db
    db.get_session().delete(address)
    db.get_session().commit()
    return redirect(url_for('address'))



# ------------------------------------- RESTAURANT ------------------------------------- #

# Create restaurant
@login_required
@api.route('/account/<int:user_id>/restaurant', methods=['POST'])
def add_restaurant(user_id):
    # check if user is restaurant owner
    if current_user.role != 'restaurant_owner':
        abort(403)
    # Get restaurant info from request
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')
    location = data.get('location')
    is_operational = data.get('is_operational')
    order_fulfilling = data.get('order_fulfilling')
    payment_methods = data.get('payment_methods')
    offers = data.get('offers')
    suppliers = data.get('suppliers')
    
    # Validate input data
    if not name or not location:
        return jsonify({'error': 'Name and location are required'}), 400
    if not isinstance(is_operational, bool):
        return jsonify({'error': 'is_operational must be a boolean'}), 400
    if not isinstance(payment_methods, list):
        return jsonify({'error': 'payment_methods must be a list'}), 400
    
    # Create a new restaurant object
    restaurant = Restaurant(
        name=name,
        description=description,
        location=location,
        is_operational=is_operational,
        order_fulfilling=order_fulfilling,
        payment_methods=payment_methods,
        offers=offers,
        suppliers=suppliers,
        created_at=datetime.utcnow()
    )

    # Add the new restaurant object to the session and commit the changes
    db.get_session().add(restaurant)
    db.get_session().commit()

    # Return a JSON response with the ID of the newly created restaurant
    return jsonify({'message': 'Restaurant created successfully', 'id': restaurant.id})


# Read restaurant for the owner
@login_required
@api.route('/dashboard/restaurant/<int:restaurant_id>', methods=['GET'])
def restaurant(restaurant_id):
    # get the restaurant from the DB
    restaurant = db.get_session().query(Restaurant).get_or_404(restaurant_id)

    # check whether the user is owner or simple user
    if current_user.role == 'restaurant_owner':
        # get all the information for the restaurant
        reservations = db.get_session().query(Reservation).filter(Reservation.restaurant_id == restaurant_id).all()
        menus = db.get_session().query(Menu).filter(Menu.restaurant_id == restaurant_id).all()
        orders = db.get_session().query(Order).filter(Order.restaurant_id == restaurant_id).all()
        shipments = db.get_session().query(Shipment).filter(Shipment.restaurant_id == restaurant_id).all()

        return jsonify({
            "id": restaurant.id,
            "name": restaurant.name,
            "description": restaurant.description,
            "location": restaurant.location,
            "is_operational": restaurant.is_operational,
            "order_fulfilling": restaurant.order_fulfilling,
            "menus": menus,
            "products": restaurant.products,
            "orders": orders,
            "payment_methods": restaurant.payment_methods,
            "reservations": reservations,
            "customers": restaurant.customers,
            "shipments": shipments,
            "offers": restaurant.offers,
            "suppliers": restaurant.suppliers,
            "created_at": restaurant.created_at,
            "updated_at": restaurant.updated_at
        })
    else:
        # get only public information for the restaurant
        return jsonify({
            "id": restaurant.id,
            "name": restaurant.name,
            "description": restaurant.description,
            "location": restaurant.location,
            "is_operational": restaurant.is_operational,
            "order_fulfilling": restaurant.order_fulfilling,
            "payment_methods": restaurant.payment_methods,
            "offers": restaurant.offers,
            "suppliers": restaurant.suppliers,
            "created_at": restaurant.created_at,
            "updated_at": restaurant.updated_at
        })

# Update restaurant
@login_required
@api.route('/account/<int:user_id>/restaurant/<int:restaurant_id>/update', methods=['PUT'])
def update_restaurant(restaurant_id):
    # check if user is restaurant owner
    if current_user.role != 'restaurant_owner':
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

@login_required
@api.route('/dashboard/restaurant/<int:restaurant_id>/delete', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    # check if user is restaurant owner
    if current_user.role != 'restaurant_owner':
        abort(403)
    # get the restaurant from the DB
    restaurant = db.get_session().query(Restaurant).get_or_404(restaurant_id)

    # delete the restaurant from the DB
    db.get_session().delete(restaurant)
    db.get_session().commit()

    return jsonify({'message': 'Restaurant deleted successfully'}), 200


# ------------------------------------- MENU ITEM ------------------------------------- #

# Create menu item
@login_required
@api.route('/account/<int:user_id>/menu_item/new', methods=['POST'], strict_slashes=False)

def add_menu_item():
    # check if user is restaurant owner
    if current_user.role != 'restaurant_owner':
        abort(403)
    # get menu item info from request
    data = request.get_json()

    menu_item = MenuItem(
        name=data.get('name'),
        description=data.get('description'),
        category=data.get('category'),
        price=data.get('price'),
        foods=data.get('foods'),
        is_available=data.get('is_available'),
        is_delivrable=data.get('is_delivrable'),
        duration_of_preparation=data.get('duration_of_preparation'),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    # Add the new menu object to the session and commit the changes
    db.get_session().add(menu_item)
    db.get_session().commit()

    # Return a JSON response
    return jsonify({'Menu item created successfully'})

# Read menu item
@login_required
@api.route('/dashboard/menu_item/<int:item_id>', methods=['GET'])
def menu_item(item_id):
    # get the menu_item from the DB
    menu_item = db.get_session().query(MenuItem).get_or_404(item_id)

    # Return them to the user
    return jsonify({
        "name": menu_item.name,
        "description": menu_item.description,
        "category": menu_item.category,
        "price": menu_item.price,
        "foods": menu_item.foods,
        "is_available": menu_item.is_available,
        "is_deliverable": menu_item.is_deliverable,
        "duration_of_preparation": menu_item.duration_of_preparation,
       })

# Update menu item
@login_required
@api.route('/account/<int:user_id>/dashboard/menu_item/<int:id>/update', methods=['PUT'])

def update_menu_item(id: int):
    # check if user is restaurant owner
    if current_user.role != 'restaurant_owner':
        abort(403)
    # get the menu_item informations from the DB
    menu_item = db.get_session().query(MenuItem).get_or_404(id)

    
    # get the menu_item info from the user and update them in the db
    data = request.get_json()

    # Update the menu item object
    if 'name' in data:
        menu_item.name = data['name']
    if 'description' in data:
        menu_item.description = data['description']
    if 'category' in data:
        menu_item.category = data['category']
    if 'price' in data:
        menu_item.price = data['price']
    if 'foods' in data:
        menu_item.foods = data['foods']
    if 'is_available' in data:
        menu_item.is_available = data['is_available']
    if 'is_deliverable' in data:
        menu_item.is_deliverable = data['is_deliverable']
    if 'duration_of_preparation' in data:
        menu_item.duration_of_preparation = data['duration_of_preparation']
    
    menu_item.updated_at = datetime.utcnow()
    
    # Commit the changes to DB
    db.get_session().commit()
    return jsonify({'Menu item updated successfully'}), 200

# Delete menu item
@login_required
@api.route('/account/<int:user_id>/dashboard/menu_item/<int:item_id>/delete', methods=['DELETE'])
def delete_menu_item(item_id):
    menu_item = db.get_session().query(MenuItem).get_or_404(item_id)

    # delete the menu item
    db.get_session().delete(menu_item)
    db.get_session().commit()
    
    return jsonify({'message': 'Menu item deleted successfully'}), 200


# ------------------------------------- MENU ------------------------------------- #

# Create Menu
@login_required
@api.route('/account/<int:user_id>/menu/new', methods=['POST'], strict_slashes=False)
def add_menu():
    # check if user is restaurant owner
    if current_user.role != 'restaurant_owner':
        abort(403)
    # Get menu info from request
    data = request.get_json()
    
    # Retrieve the restaurant by id
    restaurant_id = data.get('restaurant_id')
    restaurant = db.get_session().query(Restaurant).get_or_404(restaurant_id)
    
    # Create a new menu object
    menu = Menu(
        name=data.get('name'),
        description=data.get('description'),
        category=data.get('category'),
        items=data.get('items'),
        created_at=datetime.utcnow(),
        restaurant=restaurant
    )

    # Add the new menu object to the session and commit
    db.get_session().add(menu)
    db.get_session().commit()


    # Return a JSON response
    return jsonify({'message': 'Menu created successfully'})

# Read Menu 

@login_required
@api.route('/dashboard/menu/<int:menu_id>')
def menu(menu_id):
    menu = db.get_session().query(Menu).get_or_404(menu_id)
    menu_items = [{'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price} for item in menu.items]

    return jsonify({
        'name': menu.name,
        'description': menu.description,
        'category': menu.category,
        'menu_items': menu_items,
        'created_at': datetime.utcnow(),
        'restaurant': menu.restaurant
    })

# Update menu

@login_required
@api.route('/account/<int:user_id>/dashboard/menu/<int:menu_id>/update', methods=['PUT'])
def update_menu(menu_id):
    # check if user is restaurant owner
    if current_user.role != 'restaurant_owner':
        abort(403)
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
    if 'items' in data:
        menu.items = data['items']

    # Commit changes to DB

    db.get_session().add(menu)
    db.get_session().commit()

    # Return a JSON response
    return jsonify({'message': 'Menu updated successfully'}), 200

# Delete Menu

@login_required
@api.route('/account/<int:user_id>/menu/<int:menu_id>/delete', methods=['DELETE'])
def delete_menu(menu_id):
    menu = db.get_session().query(Menu).get_or_404(menu_id)
    
    # delete the menu
    db.get_session().delete(menu)
    db.get_session().commit()
    
    return jsonify({'message': 'Menu deleted successfully'})


# ------------------------------------- ORDER ------------------------------------- #


@login_required

@api.route('/restaurant/<int:restaurant_id>/orders', methods=['POST'])
# @roles_required('customer')
def add_order(restaurant_id):
    # Get the restaurant from the DB
    db.get_session().query(Restaurant).get_or_404(restaurant_id)

    # Parse the data from the request
    data = request.get_json()

    # Create a new Order object
    order = Order(
        restaurant_id=restaurant_id,
        user_id=current_user.id,
        items=data.get('items'),
        total_price=data.get('total_price'),
        address=data.get('address'),
        shipment_method=data.get('shipment_method'),
        payment_method=data.get('payment_method'),
        status=data.get('status'),
        notes=data.get('notes'),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    # Add the order to the DB
    db.get_session().add(order)
    db.get_session().commit()


    # Return a success message to the user
    return jsonify({'message': 'Order added successfully!'}), 201

# Read order
@login_required
@api.route('/restaurant/<int:restaurant_id>/orders/<int:order_id>', methods=['GET'])
def order(restaurant_id, order_id):
    # Get the order from the DB
    order = db.get_session().query(Order).filter(Order.restaurant_id == restaurant_id, Order.id == order_id).first()

    if not order:
        return jsonify({'error': 'Order not found'}), 404

    # Return the order to the user
    return jsonify({
        "id": order.id,
        "restaurant_id": order.restaurant_id,
        "user_id": order.user_id,
        "items": order.items,
        "total_price": order.total_price,
        "address": order.address,
        "shipment_method": order.shipment_method,
        "payment_method": order.payment_method,
        "status": order.status,
        "notes": order.notes,
        "created_at": order.created_at,
        "updated_at": order.updated_at
    })

# Update order
@login_required

@api.route('/restaurant/<int:restaurant_id>/orders/<int:order_id>', methods=['PUT'])
def update_order(restaurant_id, order_id):
    # Get the restaurant and order from the DB
    db.get_session().query(Restaurant).get_or_404(restaurant_id)
    order = db.get_session().query(Order).get_or_404(order_id)

    # Parse the data from the request
    data = request.get_json()

    # Update the order object
    if 'items' in data:
        order.items = data['items']
    if 'total_price' in data:
        order.total_price = data['total_price']
    if 'address' in data:
        order.address = data['address']
    if 'shipment_method' in data:
        order.shipment_method = data['shipment_method']
    if 'payment_method' in data:
        order.payment_method = data['payment_method']
    if 'status' in data:
        order.status = data['status']
    if 'notes' in data:
        order.notes = data['notes']
    order.updated_at = datetime.utcnow()

    # Commit the changes to the DB
    db.get_session().commit()


    # Return a success message to the user
    return jsonify({'message': 'Order updated successfully!'}), 200

# Delete order
@login_required
@api.route('/restaurant/<int:restaurant_id>/orders/<int:order_id>', methods=['DELETE'])
def delete_order(restaurant_id, order_id):
    # Get the order from the DB
    order = db.get_session().query(Order).filter(Order.restaurant_id == restaurant_id, Order.id == order_id).first()

    if not order:
        # If the order doesn't exist, return a 404 error
        return jsonify({'error': 'Order not found'}), 404

    # Remove the order from the DB

    db.get_session().delete(order)
    db.get_session().commit()

    # Return a success message to the user
    return jsonify({'message': 'Order deleted successfully!'})



# ------------------------------------- RESERVATION ------------------------------------- #


@login_required
@api.route('/restaurant/<int:restaurant_id>/reservations', methods=['POST'])
# @roles_required('customer')
def add_reservation(restaurant_id):
    # Get the restaurant from the DB
    db.get_session().query(Restaurant).get_or_404(restaurant_id)


    # Parse the data from the request
    data = request.get_json()

    # Create a new reservation object
    reservation = Reservation(
        restaurant_id=restaurant_id,
        user_id=current_user.id,
        description=data.get('description'),
        duration=data.get('duration'),
        start=data.get('start'),
        end=data.get('end'),
        nb_of_person=data.get('nb_of_person'),
        additional_info=data.get('additional_info'),
        tables=data.get('tables'),
        price=data.get('price'),
        tax=data.get('tax'),
        menu_item=data.get('menu_item'),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    # Add the reservation to the DB
    db.get_session().add(reservation)
    db.get_session().commit()

    # Return a success message to the user
    return jsonify({'message': 'Reservation added successfully!'}), 201

# Read reservation
@login_required
@api.route('/restaurant/<int:restaurant_id>/reservations/<int:reservation_id>', methods=['GET'])

def reservation(restaurant_id, reservation_id):
    # Get the reservation from the DB
    reservation = db.session.query(Reservation).filter(reservation.restaurant_id == restaurant_id, reservation.id == reservation_id).first()

    if not reservation:
        return jsonify({'error': 'Reservation not found'}), 404

    # Return the reservation to the user
    return jsonify({
        "id": reservation.id,
        "restaurant_id": reservation.restaurant_id,
        "user_id": reservation.user_id,
        "description": reservation.description,
        "duration": reservation.duration,
        "start": reservation.start,
        "end": reservation.end,
        "nb_of_person": reservation.nb_of_person,
        "tables": reservation.status,
        "category": reservation.category,
        "price": reservation.price,
        "tax": reservation.tax,
        "menu_item,": reservation.menu_item,
        "created_at": reservation.created_at,
        "updated_at": reservation.updated_at
    })

# Update reservation
@login_required
@api.route('/restaurant/<int:restaurant_id>/reservations/<int:reservation_id>', methods=['PUT'])
def update_reservation(restaurant_id, reservation_id):
    # Get the restaurant and reservation from the DB
    db.get_session().query(Restaurant).get_or_404(restaurant_id)
    reservation = db.get_session().query(reservation).get_or_404(reservation_id)
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
    if 'menu_item' in data:
        reservation.menu_item = data['menu_item']

    reservation.updated_at = datetime.utcnow()

    # Commit the changes to the DB
    db.get_session().commit()


    # Return a success message to the user
    return jsonify({'message': 'Reservation updated successfully!'}), 200

# Delete reservation
@login_required
@api.route('/restaurant/<int:restaurant_id>/reservations/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(restaurant_id, reservation_id):
    # Get the reservation from the DB
    reservation = db.get_session().query(reservation).filter(reservation.restaurant_id == restaurant_id, reservation.id == reservation_id).first()
    if not reservation:
        # If the reservation doesn't exist, return a 404 error
        return jsonify({'error': 'Reservation not found'}), 404

    # Remove the reservation from the DB

    db.get_session().delete(reservation)
    db.get_session().commit()


    # Return a success message to the user
    return jsonify({'message': 'Reservation deleted successfully!'})