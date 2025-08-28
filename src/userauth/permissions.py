from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Return true (full access) for admin users; false (read-only) for everyone else.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
