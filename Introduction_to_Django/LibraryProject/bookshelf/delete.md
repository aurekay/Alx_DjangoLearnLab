from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four", author="George Orwell", publication_year=1949)
book.delete()  # Expected: (1, {'bookshelf.Book': 1})

list(Book.objects.all())
# Expected: []  (empty list after deletion)
