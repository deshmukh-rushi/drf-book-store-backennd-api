from rest_framework import serializers
from app1.models import Author,Book,Genre,Purchase,Review
from django.contrib.auth.models import User
from rest_framework.reverse import reverse


#Nested Serializer


from rest_framework import serializers
from rest_framework.reverse import reverse
from app1.models import Book

class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name', read_only=True)
    genre = serializers.CharField(source='genre.name', read_only=True)
    reviews_url = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'description', 'price', 'stock', 'created_at', 'updated_at', 'reviews_url']

    def get_reviews_url(self, obj):
        # Now, this will generate the URL using 'review-list' which is registered above
        return reverse('review-list', request=self.context.get('request'), kwargs={'book_id': obj.id})



##########################################################
class BookTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookTitleSerializer(many = True,read_only = True)
    class Meta:
        model = Author
        fields = ['id','name','bio','created_at','updated_at','books']

###########################################################





class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name','description']




class PurchaseSerializer(serializers.ModelSerializer):
    buyer = serializers.CharField(source='buyer.username', read_only=True)
    book = serializers.CharField(source='book.title', read_only=True)
    purchase_date = serializers.DateTimeField(format="%d %B %Y, %I:%M %p")
    class Meta:
        model = Purchase
        fields = ['id','buyer','book','quantity','purchase_date']




class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    book_name = serializers.CharField(source='book.title', read_only=True)
    # book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.none())

    class Meta:
        model = Review
        fields = ['id', 'user', 'book','book_name', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user

        if user.is_authenticated:
            purchased_books = Purchase.objects.filter(buyer=user).values_list('book', flat=True)
            self.fields['book'].queryset = Book.objects.filter(id__in=purchased_books)

    def validate(self, data):
        user = self.context['request'].user
        book = data['book']

        # Check if the user has purchased the book
        if not Purchase.objects.filter(buyer=user, book=book).exists():
            raise serializers.ValidationError("You can only review books you have purchased.")

        # Check if the user has already reviewed the book
        if Review.objects.filter(user=user, book=book).exists():
            raise serializers.ValidationError("You have already reviewed this book.")

        return data
