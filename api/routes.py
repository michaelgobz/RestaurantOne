from flask import Blueprint, request, session, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
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

# Authentication

@app.route('/auth/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    # if request.method == 'GET':
    #     return render_template('signup.html')

    # get user info from request
    email = request.json.get('email')
    password = request.json.get('password')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')

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