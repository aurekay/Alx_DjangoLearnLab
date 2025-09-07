
import os
import sys
from pathlib import Path

# Ensure project root on sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

import django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def samples():
    author_name = "George Orwell"
    library_name = "Central Library"

    # --- Seed data ---
    Author.objects.get_or_create(name=author_name)
    author = Author.objects.get(name=author_name)
    book1, _ = Book.objects.get_or_create(title="1984", author=author)
    book2, _ = Book.objects.get_or_create(title="Animal Farm", author=author)

    library, _ = Library.objects.get_or_create(name=library_name)
    library.books.add(book1, book2)
    Librarian.objects.get_or_create(name="Alice Smith", library=library)

    # 1) Query all books by a specific author
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print("Books by", author_name, ":", list(books_by_author.values_list("title", flat=True)))

    # 2) List all books in a library
    lib_obj = Library.objects.get(name=library_name)
    books_in_library = lib_obj.books.all()
    print("Books in", library_name, ":", list(books_in_library.values_list("title", flat=True)))

    # 3) Retrieve the librarian for a library
    librarian = Library.objects.get(name=library_name).librarian
    print("Librarian for", library_name, ":", librarian.name)

if __name__ == "__main__":
    samples()
