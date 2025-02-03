# permissions.py
from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only staff members to edit.
    Non-staff members can only view the data.
    """

    def has_permission(self, request, view):
        # If the request method is a safe method (like GET, HEAD, or OPTIONS), allow it for anyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, check if the user is a staff member
        return request.user and request.user.is_staff
