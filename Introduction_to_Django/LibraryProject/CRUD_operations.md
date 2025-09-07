``python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.id 
from bookshelf.models import Book
book = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
(book.title, book.author, book.publication_year)
from bookshelf.models import Book
book = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
book.title = "Nineteen Eighty-Four"
book.save()
book.refresh_from_db()
book.title 
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four", author="George Orwell", publication_year=1949)
book.delete()  # Expected: (1, {'bookshelf.Book': 1})

list(Book.objects.all())
