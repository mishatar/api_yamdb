import logging

from rest_framework import permissions

logging.basicConfig(
    level=logging.DEBUG,
    filename='program.log'
)


class IsAdminCustomUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            request.user.is_authenticated
            and (request.user.is_admin)
        ):
            return True
        return True


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.method == 'POST'
                or request.method == 'DELETE'
                or request.method == 'PATCH'
                ) and (
                    request.user.is_authenticated
                    and request.user.is_admin)


class IsAdminOrAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and (
            request.user.is_admin
            or request.user.is_moderator
            or request.user == obj.author)
