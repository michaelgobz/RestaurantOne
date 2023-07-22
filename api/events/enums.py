""" Events enum"""

from enum import Enum

class BaseEventEnum(Enum):
    """Base event"""
    @property
    def codename(self):
        """return the event codename"""
        return self.value.split(".")[1]


class AccountEvents(BaseEventEnum):
    """account Events"""
    MANAGE_USERS = "account.manage_users"
    MANAGE_STAFF = "account.manage_staff"
    IMPERSONATE_USER = "account.impersonate_user"



class MenuEvents(BaseEventEnum):
    MANAGE_MENUS = "menu.manage_menus"


class CheckoutEvents(BaseEventEnum):
    MANAGE_CHECKOUTS = "checkout.manage_checkouts"
    HANDLE_CHECKOUTS = "checkout.handle_checkouts"
    HANDLE_TAXES = "checkout.handle_taxes"
    MANAGE_TAXES = "checkout.manage_taxes"

class ReservationEvents(BaseEventEnum):
    """Reservation Events"""
    MANAGE_RESERVATIONS = 'reservation.manage_reservation'

class OrderEvents(BaseEventEnum):
    """Order  Events"""
    MANAGE_ORDERS = "order.manage_orders"


class PaymentEvents(BaseEventEnum):
    """payments Events"""
    HANDLE_PAYMENTS = "payment.handle_payments"



class ProductEvents(BaseEventEnum):
    """Product Events"""
    MANAGE_PRODUCTS = "product.manage_products"


class ProductTypeEvents(BaseEventEnum):
    """product type Events"""
    MANAGE_PRODUCT_TYPES_AND_ATTRIBUTES = "product.manage_product_types_and_attributes"


class ShippingEvents(BaseEventEnum):
    """shipping Events"""
    MANAGE_SHIPPING = "shipping.manage_shipping"




Events_ENUMS = [
    AccountEvents,
    CheckoutEvents,
    MenuEvents,
    ReservationEvents,
    OrderEvents,
    PaymentEvents,
    ProductEvents,
    ProductTypeEvents,
    ShippingEvents,
]


def get_events_codename():
    """get the event codename"""
    events_values = [
        enum.codename
        for event_enum in Events_ENUMS
        for enum in event_enum
    ]
    return events_values


def get_events_enum_list():
    """get the Events enum"""
    events_list = [
        (enum.name, enum.value)
        for event_enum in Events_ENUMS
        for enum in event_enum
    ]
    return events_list


def get_events_enum_dict():
    """get the Events enmu dict"""
    return {
        enum.name: enum
        for event_enum in Events_ENUMS
        for enum in event_enum
    }

# these are Events need an used hand in hand with the flask_Events
