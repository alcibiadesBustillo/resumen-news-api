from rest_framework import permissions


class BasePermission(object):
    """
    A base class from which all permission classes should inherit
    """

    def has_permission(self, request, view):
        """
        Return 'True' if permission is granted, 'False' otherwise
        """ 

        return True
    
    def has_object_permission(self, request, view, obj):
        """
        Return 'True' if permission is granted, 'False' otherwise
        """ 

        return True

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any reuqest
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write permissions are only allowed to the author of a news
        return obj.author == request.user

    
    