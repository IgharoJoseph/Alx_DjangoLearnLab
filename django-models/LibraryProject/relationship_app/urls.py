from django.urls import path
from .views import (
    list_books, LibraryDetailView, home_view,
    register_view, login_view, logout_view
)

urlpatterns = [
    # Existing views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', home_view, name='home'),
    
    # Authentication views
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
