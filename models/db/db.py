"""DB module
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from .models import Base, User, Restaurants, Menus, MenuItems, Products, Reservations, Orders


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine('sqlite:///resto.db', echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            db_session = sessionmaker(bind=self._engine)
            self.__session = db_session()
        return self.__session
    
    def add_user(self, email: str, hashed_password: str, **kwargs) -> User:
        """ Saves the user to the database and
        Returns a User object
        """
        new_user = User(email=email, hashed_password=hashed_password, **kwargs)
        
        self._session.add(new_user)
        self._session.commit()

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Returns the first row found in the users table
        as filtered by the methods input arguments
        """
        if not kwargs:
            raise InvalidRequestError

        column_keys = User.__table__.columns.keys()

        for key in kwargs.keys():
            if key not in column_keys:
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Locate user to update and update the user's attributes
        as passed in the method's argument, then commit the changes
        to the database
        """
        if not kwargs:
            return None

        user = self.find_user_by(id=user_id)

        column_keys = User.__table__.columns.keys()

        for key in kwargs.keys():
            if key not in column_keys:
                raise ValueError

        for key, value in kwargs.items():
            setattr(user, key, value)

        self._session.commit()


        #### RESTAURANT ####

    def add_restaurant(self, *args):
        """Saves the restaurant to the database
        """
        restaurant = Restaurants(*args)

        self._session.add(restaurant)
        self._session.commit()

    def find_restaurant_by(self, *args) -> Restaurants:
        """ Returns the first row found in the Restaurants table
        as filtered by the methods input arguments
        """
        if not args:
            raise InvalidRequestError

        column_keys = Restaurants.__table__.columns.keys()

        for arg in args:
            if arg not in column_keys:
                raise InvalidRequestError

        restaurant = self._session.query(Restaurants).filter_by(*args).first()

        if restaurant is None:
            raise NoResultFound

        return restaurant
    

    #### Product ####

    def add_product(self, *args):
        """Saves the products to the database
        """
        product = Products(*args)

        self.__session.add(product)
        self.__session.commit()

    def find_product_by(self, *args) -> Products:
        """ Returns the first row found in the Products table
        as filtered by the methods input arguments
        """
        if not args:
            raise InvalidRequestError

        column_keys = Products.__table__.columns.keys()

        for arg in args:
            if arg not in column_keys:
                raise InvalidRequestError

        product = self._session.query(Products).filter_by(*args).first()

        if product is None:
            raise NoResultFound

        return product
    

    #### Menu ####

    def add_menu(self, *args):
        """Saves the menu to the database
        """
        menu = Menus(*args)

        self.__session.add(menu)
        self.__session.commit()

    def find_menu_by(self, *args) -> Menus:
        """ Returns the first row found in the Menus table
        as filtered by the methods input arguments
        """
        if not args:
            raise InvalidRequestError

        column_keys = Menus.__table__.columns.keys()

        for arg in args:
            if arg not in column_keys:
                raise InvalidRequestError

        menu = self._session.query(Menus).filter_by(*args).first()

        if menu is None:
            raise NoResultFound

        return menu


    #### Menu item ####

    def add_menu_item(self, *args):
        """Saves the menu items to the database
        """
        menu_item = MenuItems(*args)

        self.__session.add(menu_item)
        self.__session.commit()

    def find_menu_item_by(self, *args) -> MenuItems:
        """ Returns the first row found in the MenuItems table
        as filtered by the methods input arguments
        """
        if not args:
            raise InvalidRequestError

        column_keys = MenuItems.__table__.columns.keys()

        for arg in args:
            if arg not in column_keys:
                raise InvalidRequestError

        menu_items = self._session.query(MenuItems).filter_by(*args).first()

        if menu_items is None:
            raise NoResultFound

        return menu_items



        #### Order ####

    def add_order(self, *args):
        """Saves the menu to the database
        """
        order = Orders(*args)

        self.__session.add(order)
        self.__session.commit()

    def find_order_by(self, *args) -> Orders:
        """ Returns the first row found in the Orders table
        as filtered by the methods input arguments
        """
        if not args:
            raise InvalidRequestError

        column_keys = Orders.__table__.columns.keys()

        for arg in args:
            if arg not in column_keys:
                raise InvalidRequestError

        order = self._session.query(Orders).filter_by(*args).first()

        if order is None:
            raise NoResultFound

        return order


    #### Reservation ####

    def add_reservation(self, *args):
        """Saves the menu to the database
        """
        reservation = Reservations(*args)

        self.__session.add(reservation)
        self.__session.commit()

    def find_reservation_by(self, *args) -> Reservations:
        """ Returns the first row found in the Reservations table
        as filtered by the methods input arguments
        """
        if not args:
            raise InvalidRequestError

        column_keys = Reservations.__table__.columns.keys()

        for arg in args:
            if arg not in column_keys:
                raise InvalidRequestError

        reservation = self._session.query(Reservations).filter_by(*args).first()

        if reservation is None:
            raise NoResultFound

        return reservation