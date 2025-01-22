# from rest_framework.permissions import BasePermission, SAFE_METHODS


# class IsOwnerOrReadOnly(BasePermission):
#     """
#     Custom permission to allow only the owner of the review to update it.
#     Others can only read (GET) the data.
#     """
#     def has_permission(self, request, view):
#         # Allow safe methods (GET, HEAD, OPTIONS) for all users
#         if request.method in SAFE_METHODS:
#             return True
#         # Allow update only if the user is authenticated and the review belongs to the user
#         return request.user.is_authenticated and request.method in ['PUT', 'PATCH']

#     def has_object_permission(self, request, view, obj):
#         # For non-safe methods (i.e., PUT/PATCH), ensure the user can only modify their own review
#         if request.method in ['PUT', 'PATCH']:
#             return obj.user == request.user  # Allow modification only if the user is the owner of the review
#         return True


from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsReadOnlyOrReview(BasePermission):
    """
    Custom permission to allow only review posting for users, and read-only for other APIs.
    """

    def has_permission(self, request, view):
        # Allow read-only access for all users
        if request.method in SAFE_METHODS:
            return True

        # Allow modifications only for the Review model
        return view.basename == 'review'
