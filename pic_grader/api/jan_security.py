from rest_framework import permissions

class HasAPIKey(permissions.BasePermission):
    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_X_API_KEY')
        # print(api_key)
        return api_key == 'xdxd'
