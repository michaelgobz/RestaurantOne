""" The authentication controller for all controllers in the api """


import os
from uuid import uuid4
from datetime import datetime
import bcrypt
from jwt import decode, encode
from flask import jsonify
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError 
from ..models import User, VerificationToken
from .base_controller import BaseController


class AuthController:
    """ The authentication controller for all controllers in the api """
    _controller:BaseController = None

    def __init__(self, controller:BaseController):
        """ The constructor for the authentication controller. """
        self._controller = controller

    def get_controller(self):
        """ The get method for the authentication controller. """
        return self._controller

    def signup(self):
        """Sign up a new user"""
        # get user info from request
        data = self.get_controller().get_request().get_json()

        password = data.get('password')

        # generate salt and hash the password
        salt = bcrypt.gensalt(rounds=12, prefix=b'2b')
        salt_to_string = salt.decode('utf-8')
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

    # create a new user object
        new_user = User(id=str(uuid4()),
                        email=data.get('email'),
                        password=password_hash.decode('utf-8'),
                        first_name=data.get('firstname'),
                        last_name=data.get('lastname'),
                        role='customer',
                        salt=salt_to_string,
                        phone_number=data.get('Phonenumber'),
                        created_at=datetime.utcnow(),
                        updated_at=datetime.utcnow())

        # try to add user to database
        try:
            self.get_controller().get_db_client().get_session().add(new_user)

            # generate verification token
            new_user_created = self.get_controller().get_db_client()\
                .get_session().query(User).\
                filter_by(email=data.get('email')).first()
            token = encode({'email': new_user_created.email},
                           os.environ.get('SECRET_KEY'), algorithm="HS256")
            # send verification email

            # store the verification token in the database
            user_verification_token = VerificationToken(id=str(uuid4()),
                                                        token=token,
                                                        created_at=datetime.utcnow(),
                                                        user_id=new_user.id)
            self.get_controller().get_db_client().get_session().add(user_verification_token)
            self.get_controller().get_db_client().get_session().commit()

            return jsonify({'message': 'user created successfully',
                        'redirect': 'login',
                        'details': 'check your email to confirm your account',
                        'token': token})
        except IntegrityError:
            self.get_controller().get_db_client().get_session().rollback()

            return jsonify({'error':
                            'Email already registered  or server error or token error'})


    def login(self):
        """ login method to authenticate users"""
        # get user info from request
        email = self.get_controller().get_request().json.get('email')
        password = self.get_controller().get_request().json.get('password')

        # query the user email and password
        user = self.get_controller().get_db_client().get_session()\
        .query(User).filter_by(email=email).first()
        # hash the password and compare with the password in the database
        if user is None:
            return jsonify({'error': 'Incorrect email or password'}), 401
        else:
            salt = user.salt
        user_password = user.password
        #b = bytes(user_password,'utf-8')
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
        
    def confirm_account(self, token:str):
        """ confirm account method to authenticate users"""
        # get user info from request
       

        payload = decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
        email = payload['email']
        user = self.get_controller().get_db_client().get_session()\
            .query(User).filter_by(email=email).first()
        if user:
            user.is_verified = True
            self.get_controller().get_db_client().get_session().commit()
            return jsonify({'message': 'Account confirmed successfully',
                        'redirect': 'login',
                        'details': 'welcome to the Restaurant One'})
        else:
            return jsonify({'error': 'Account not found'})
        
        