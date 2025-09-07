from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: plain-text list of books and authors
def list_books(request):
    lines = [f"{b.title} by {b.author.name}" for b in Book.objects.select_related("author").all()]
    return HttpResponse("\n".join(lines) or "No books available.", content_type="text/plain")

# Class-based view: library detail with its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # optional template
    context_object_name = "library"
