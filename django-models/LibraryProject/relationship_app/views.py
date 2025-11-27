from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book  

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view: show details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # Must explicitly use Library
    template_name = 'relationship_app/library_detail.html'  # Must include 'relationship_app/' in path
    context_object_name = 'library'
