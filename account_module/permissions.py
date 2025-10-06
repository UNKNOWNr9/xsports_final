from .models import CustomUser
from rest_framework.permissions import BasePermission


class BlockedUserPermission(BasePermission):
    def has_permission(self, request, view):
        blocked_user = CustomUser.objects.filter(username='admin').exists()
        if blocked_user:
            return not blocked_user
