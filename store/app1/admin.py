from django.contrib import admin
from .models import Author, Purchase, Book, Genre, Review

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'bio', 'created_at', 'updated_at']


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer', 'book', 'quantity', 'purchase_date']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'rating', 'comment', 'created_at']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'get_genres', 'description', 'price', 'stock', 'created_at', 'updated_at']
    #raw_id_fields = ('genre',)  # Use raw_id_fields to display genre as a clickable field

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])
    get_genres.short_description = 'Genres'  # Custom label for the genres column
     
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):  # Corrected here
    list_display = ['id', 'name', 'description']
