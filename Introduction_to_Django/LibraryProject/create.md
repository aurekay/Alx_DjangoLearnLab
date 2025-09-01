### Create a Book instance

```python
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b

<Book: 1984 by George Orwell (1949)>

