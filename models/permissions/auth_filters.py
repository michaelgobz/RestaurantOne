"""Authorization filters for the permissions system."""

from .enums import BasePermissionEnum


def is_user(context):
    user = context.user
    return user and user.is_active


def is_operator_user(context):
    return is_user(context) and context.user.is_operator


class AuthorizationFilters(BasePermissionEnum):
    # Grants access to any authenticated staff user.
    AUTHENTICATED_RESTAURANT_OWNER = "authorization_filters.authenticated_operator_user"

    # Grants access to any authenticated user.
    AUTHENTICATED_USER = "authorization_filters.authenticated_user"

    # Grants access to the owner of the related object. This rule doesn't come with any
    # permission function, as the ownership needs to be defined individually in each
    # case.
    OWNER = "authorization_filters.owner"


AUTHORIZATION_FILTER_MAP = {
    AuthorizationFilters.AUTHENTICATED_RESTAURANT_OWNER: is_operator_user,
    AuthorizationFilters.AUTHENTICATED_USER: is_user,
}


def resolve_authorization_filter_fn(perm):
    return AUTHORIZATION_FILTER_MAP.get(perm)
