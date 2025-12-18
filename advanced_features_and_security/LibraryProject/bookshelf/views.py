from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.http import HttpResponse
from .forms import ExampleForm

def book_list(request):
    # Using Django ORM to prevent SQL injection
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def secure_book_create(request):
    # Using Django forms for input validation and sanitization
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})


def csp_protected_view(request):
    response = HttpResponse("CSP Protected Content")
    response['Content-Security-Policy'] = "default-src 'self'"
    return response
