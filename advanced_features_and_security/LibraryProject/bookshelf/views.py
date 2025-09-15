from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

@permission_required("bookshelf.can_view", raise_exception=True)
def list_books_bs(request):
    return HttpResponse("List Books (bookshelf)")

@permission_required("bookshelf.can_create", raise_exception=True)
def add_book_bs(request):
    return HttpResponse("Add Book (bookshelf)")

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book_bs(request):
    return HttpResponse("Edit Book (bookshelf)")

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book_bs(request):
    return HttpResponse("Delete Book (bookshelf)")
