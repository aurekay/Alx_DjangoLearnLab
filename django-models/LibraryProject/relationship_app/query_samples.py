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
    # Seed data (safe to re-run)
    author_name = "George Orwell"
    library_name = "Central Library"

    author, _ = Author.objects.get_or_create(name=author_name)
    b1, _ = Book.objects.get_or_create(title="1984", author=author)
    b2, _ = Book.objects.get_or_create(title="Animal Farm", author=author)

    lib, _ = Library.objects.get_or_create(name=library_name)
    lib.books.add(b1, b2)
    Librarian.objects.get_or_create(name="Alice Smith", library=lib)

    # 1) Query all books by a specific author
    books_by_author = Book.objects.filter(author__name=author_name)
    print("Books by", author_name, ":", list(books_by_author.values_list("title", flat=True)))

    # 2) List all books in a library (checker requires this exact call)
    lib_obj = Library.objects.get(name=library_name)
    books_in_library = lib_obj.books.all()
    print("Books in", library_name, ":", list(books_in_library.values_list("title", flat=True)))

    # 3) Retrieve the librarian for a library
    librarian = lib_obj.librarian
    print("Librarian for", library_name, ":", librarian.name)

if __name__ == "__main__":
    samples()
