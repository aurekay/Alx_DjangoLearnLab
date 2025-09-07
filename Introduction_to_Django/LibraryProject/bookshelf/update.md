from bookshelf.models import Book
book = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
book.title = "Nineteen Eighty-Four"
book.save()
book.refresh_from_db()
book.title  # Expected: 'Nineteen Eighty-Four'
