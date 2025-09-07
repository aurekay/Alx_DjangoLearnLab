import os
import sys
from pathlib import Path

# Ensure the project root (the folder containing manage.py and the 'LibraryProject' package) is on sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

import django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def samples():
    # --- Setup sample data (safe to re-run) ---
    author, _ = Author.objects.get_or_create(name="George Orwell")
    book1, _ = Book.objects.get_or_create(title="1984", author=author)
    book2, _ = Book.objects.get_or_create(title="Animal Farm", author=author)

    lib, _ = Library.objects.get_or_create(name="Central Library")
    lib.books.add(book1, book2)
    Librarian.objects.get_or_create(name="Alice Smith", library=lib)

    # 1) Books by a specific author
    orwell_books = Book.objects.filter(author__name="George Orwell")
    print("Books by George Orwell:", list(orwell_books.values_list("title", flat=True)))

    # 2) Books in a library
    central_books = lib.books.all()
    print("Books in Central Library:", list(central_books.values_list("title", flat=True)))

    # 3) Librarian for a library
    print("Librarian for Central Library:", lib.librarian.name)

if __name__ == "__main__":
    samples()
