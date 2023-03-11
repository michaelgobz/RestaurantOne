""" permissions enums """

from enum import Enum
from typing import Iterable, List


class BasePermissionEnum(Enum):
    @property
    def codename(self):
        return self.value.split(".")[1]


class AccountPermissions(BasePermissionEnum):
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


class OrderPermissions(BasePermissionEnum):
    MANAGE_ORDERS = "order.manage_orders"


class PaymentPermissions(BasePermissionEnum):
    HANDLE_PAYMENTS = "payment.handle_payments"



class ProductPermissions(BasePermissionEnum):
    MANAGE_PRODUCTS = "product.manage_products"


class ProductTypePermissions(BasePermissionEnum):
    MANAGE_PRODUCT_TYPES_AND_ATTRIBUTES = "product.manage_product_types_and_attributes"


class ShippingPermissions(BasePermissionEnum):
    MANAGE_SHIPPING = "shipping.manage_shipping"




PERMISSIONS_ENUMS = [
    AccountPermissions,
    CheckoutPermissions,
    MenuPermissions,
    OrderPermissions,
    PaymentPermissions,
    ProductPermissions,
    ProductTypePermissions,
    ShippingPermissions,
]


def get_permissions_codename():
    permissions_values = [
        enum.codename
        for permission_enum in PERMISSIONS_ENUMS
        for enum in permission_enum
    ]
    return permissions_values


def get_permissions_enum_list():
    permissions_list = [
        (enum.name, enum.value)
        for permission_enum in PERMISSIONS_ENUMS
        for enum in permission_enum
    ]
    return permissions_list


def get_permissions_enum_dict():
    return {
        enum.name: enum
        for permission_enum in PERMISSIONS_ENUMS
        for enum in permission_enum
    }

# these are permissions need an used hand in hand with the flask_permissions
