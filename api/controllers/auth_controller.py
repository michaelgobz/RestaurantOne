""" The authentication controller for all controllers in the api """


import os
import bcrypt
from uuid import uuid4
from datetime import datetime
from jwt import encode
from flask import jsonify
from sqlalchemy.exc import IntegrityError
from ..models import User, VerificationToken
from .base_controller import api_controller as Controller


class AuthController:
    """ The authentication controller for all controllers in the api """

    def signup(self):
        """ The signup method for the authentication controller. """
        """Sign up a new user"""
        # get user info from request
        data = Controller.get_request.get_json()

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
            Controller.get_db_client.get_session().add(new_user)

            # generate verification token
            new_user_created = Controller.get_db_client.get_session().query(User). \
                filter_by(email=data.get('email')).first()
            token = encode({'email': new_user_created.email},
                           os.environ.get('SECRET_KEY'), algorithm="HS256")
            # send verification email

            # store the verification token in the database
            user_verification_token = VerificationToken(id=str(uuid4()),
                                                        token=token,
                                                        created_at=datetime.utcnow(),
                                                        user_id=new_user.id)
            Controller.get_db_client.get_session().add(user_verification_token)
            Controller.get_db_client.get_session().commit()

            return jsonify({'message': 'user created successfully',  # noqa: F706
                        'redirect': 'login',
                        'details': 'check your email to confirm your account',
                        'token': token})
        except IntegrityError:
            Controller.get_db_client.get_session().rollback()

            return jsonify({'error':
                            'Email already registered  or server error or token error'})