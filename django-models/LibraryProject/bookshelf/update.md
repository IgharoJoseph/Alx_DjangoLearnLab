# UPDATE Operation

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output:
# Updated title to "Nineteen Eighty-Four"
