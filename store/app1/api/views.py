from django.shortcuts import render
from rest_framework import viewsets,permissions,serializers
from app1.models import Author,Book,Genre,Purchase,Review
from app1.api.serializers import AuthorSerializer,BookSerializer,ReviewSerializer,GenreSerializer,PurchaseSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser
from .permission import IsStaffOrReadOnly
# Create your views here.

#ModelViewSet
# @method_decorator(csrf_exempt, name='dispatch')
class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    search_fields = ['id','name']
    permission_classes = [IsStaffOrReadOnly]



class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    search_fields = ['id','title']
    permission_classes = [IsStaffOrReadOnly]

   
    


class GenreModelViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    search_fields = ['id','name']
    permission_classes = [IsStaffOrReadOnly]



class PurchaseModelViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    search_fields = ['id']
    permission_classes = [IsAdminUser]


class ReviewModelViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Show all reviews for any book.
        But, users can only create a review for the books they've purchased.
        """
        user = self.request.user
        if user.is_authenticated:
            # If the user is authenticated, show all reviews.
            return Review.objects.all()
        return Review.objects.none()
    def perform_create(self, serializer):
        user = self.request.user
        book = serializer.validated_data['book']

        # Validate if the buyer has purchased the book
        if not Purchase.objects.filter(buyer=user, book=book).exists():
            raise serializers.ValidationError("You can only review books you have purchased.")
        

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        if book_id:
            return Review.objects.filter(book_id=book_id)
        return Review.objects.all()
        # Save the review
        serializer.save(user=user)
