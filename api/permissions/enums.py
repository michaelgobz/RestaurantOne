""" permissions enums """

from enum import Enum

class BasePermissionEnum(Enum):
    """Base permission"""
    @property
    def codename(self):
        """return the permission codename"""
        return self.value.split(".")[1]


class AccountPermissions(BasePermissionEnum):
    """account permissions"""
    MANAGE_USERS = "account.manage_users"
    MANAGE_STAFF = "account.manage_staff"
    IMPERSONATE_USER = "account.impersonate_user"



class MenuPermissions(BasePermissionEnum):
    MANAGE_MENUS = "menu.manage_menus"


class CheckoutPermissions(BasePermissionEnum):
    MANAGE_CHECKOUTS = "checkout.manage_checkouts"
    HANDLE_CHECKOUTS = "checkout.handle_checkouts"
    HANDLE_TAXES = "checkout.handle_taxes"
    MANAGE_TAXES = "checkout.manage_taxes"

class ReservationPermissions(BasePermissionEnum):
    """Reservation Permissions"""
    MANAGE_RESERVATIONS = 'reservation.manage_reservation'

class OrderPermissions(BasePermissionEnum):
    """Order  permissions"""
    MANAGE_ORDERS = "order.manage_orders"


class PaymentPermissions(BasePermissionEnum):
    """payments permissions"""
    HANDLE_PAYMENTS = "payment.handle_payments"



class ProductPermissions(BasePermissionEnum):
    """Product permissions"""
    MANAGE_PRODUCTS = "product.manage_products"


class ProductTypePermissions(BasePermissionEnum):
    """product type permissions"""
    MANAGE_PRODUCT_TYPES_AND_ATTRIBUTES = "product.manage_product_types_and_attributes"


class ShippingPermissions(BasePermissionEnum):
    """shipping permissions"""
    MANAGE_SHIPPING = "shipping.manage_shipping"




PERMISSIONS_ENUMS = [
    AccountPermissions,
    CheckoutPermissions,
    MenuPermissions,
    ReservationPermissions,
    OrderPermissions,
    PaymentPermissions,
    ProductPermissions,
    ProductTypePermissions,
    ShippingPermissions,
]


def get_permissions_codename():
    """get the permissions codename"""
    permissions_values = [
        enum.codename
        for permission_enum in PERMISSIONS_ENUMS
        for enum in permission_enum
    ]
    return permissions_values


def get_permissions_enum_list():
    """get the permissions enum"""
    permissions_list = [
        (enum.name, enum.value)
        for permission_enum in PERMISSIONS_ENUMS
        for enum in permission_enum
    ]
    return permissions_list


def get_permissions_enum_dict():
    """get the permissions enmu dict"""
    return {
        enum.name: enum
        for permission_enum in PERMISSIONS_ENUMS
        for enum in permission_enum
    }

# these are permissions need an used hand in hand with the flask_permissions
