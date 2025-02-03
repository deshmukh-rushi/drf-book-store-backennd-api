from django.urls import path, include
from app1.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# Register the views with the router
router.register('AuthorAPI', views.AuthorModelViewSet, basename='author')
router.register('BookAPI', views.BookModelViewSet, basename='book')
router.register('GenreAPI', views.GenreModelViewSet, basename='genre')
router.register('PurchaseAPI', views.PurchaseModelViewSet, basename='purchase')
router.register('ReviewAPI', views.ReviewModelViewSet, basename='review')

# Define the review URL pattern with book_id as parameter
urlpatterns = [
    path('', include(router.urls)),
    path('review/<int:book_id>/', views.ReviewModelViewSet.as_view({'get': 'list'}), name='review-list'),
    path('auth/', include('rest_framework.urls')),
]
