from rest_framework import permissions, status
from rest_framework.exceptions import APIException


class GenericException(APIException):

    """
        Generic exception with custom message
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'error'

    def __init__(self, msg, code=status.HTTP_200_OK):

        self.status_code = code
        self.detail = msg


class isAuthenticated(permissions.IsAuthenticated):

    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True
        raise GenericException({
            "status": False,
            "code": status.HTTP_200_OK,
            "message": 'User not authenticated!',
            "data": {}
        })


class isVerified(permissions.IsAuthenticated):

    def has_permission(self, request, view):

        if request.user.verify:
            return True
        raise GenericException({
            "status": False,
            "code": status.HTTP_200_OK,
            "message": 'User not verfied!',
            "data": {}
        })
