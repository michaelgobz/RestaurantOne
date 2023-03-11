"""Defines the permissions protocol provided with methods to check permissions."""

from typing import  Collection

from .auth_filters import (
    AuthorizationFilters,
    is_operator_user,
    is_user,
    resolve_authorization_filter_fn,
)
from .enums import (
    PERMISSIONS_ENUMS,
    AccountPermissions,
    BasePermissionEnum,
    CheckoutPermissions,
    MenuPermissions,
    OrderPermissions,
    PaymentPermissions,
    ProductPermissions,
    ProductTypePermissions,
    ShippingPermissions,
    get_permissions_codename,
    get_permissions_enum_dict,
    get_permissions_enum_list,

)
__all__ = [
    "PERMISSIONS_ENUMS",
    "is_operator_user",
    "is_user",
    "AccountPermissions"
    "CheckoutPermissions",
    "MenuPermissions",
    "OrderPermissions",
    "PaymentPermissions",
    "ProductPermissions",
    "ProductTypePermissions",
    "ShippingPermissions",
    "get_permissions_codename",
    "get_permissions_enum_dict",
    "get_permissions_enum_list",
]


def get_user_from_context(context):
    # order is important
    # user if None then is passed as anonymous
    # more users could be returned
    return context.user


# TODO: Tailor this class round the user model considering the a tight context instance

def one_of_permissions_or_auth_filter_required(context, permissions):
    """Determine whether user  has rights to perform an action.

    The `context` parameter is the Context instance associated with the request.
    """
    if not permissions:
        return True

    authorization_filters = [
        p for p in permissions if isinstance(p, AuthorizationFilters)
    ]
    permissions = [p for p in permissions if not isinstance(
        p, AuthorizationFilters)]

    granted_by_permissions = False
    granted_by_authorization_filters = False

    requestor = get_user_from_context(context)

    if requestor and permissions:
        perm_checks_results = []
        for permission in permissions:
            perm_checks_results.append(requestor.has_perm(permission))
        granted_by_permissions = any(perm_checks_results)

    if authorization_filters:
        auth_filters_results = []
        for p in authorization_filters:
            perm_fn = resolve_authorization_filter_fn(p)
            if perm_fn:
                res = perm_fn(context)
                auth_filters_results.append(bool(res))
        granted_by_authorization_filters = any(auth_filters_results)

    return granted_by_permissions or granted_by_authorization_filters


def permission_required(
    requestor: object, perms: Collection[BasePermissionEnum]
) -> bool:
    # get the instance of User
    User = {}  # just a mock
    if isinstance(requestor, User):
        return requestor.has_perms(perms)
    elif requestor:
        if AccountPermissions.MANAGE_STAFF in perms:
            return False
        return requestor.has_perms(perms)
    return False


def has_one_of_permissions(
    requestor: object, permissions: Collection[BasePermissionEnum]
) -> bool:
    if not permissions:
        return True
    for perm in permissions:
        if permission_required(requestor, (perm,)):
            return True
    return False


def message_one_of_permissions_required(
    permissions: Collection[BasePermissionEnum],
) -> str:
    permission_msg = ", ".join([p.name for p in permissions])
    return f"\n\nRequires one of the following permissions: {permission_msg}."
