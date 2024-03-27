from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to edit their own profile"""
        #return super().has_object_permission(request, view, obj)

        # if request is GET, let user proceed
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # check if the passed obj id is same as currently authenticated user
        return obj.id == request.user.id