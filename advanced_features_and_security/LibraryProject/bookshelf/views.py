from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    return HttpResponse("Book list view (requires can_view permission)")

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    return HttpResponse("Book create view (requires can_create permission)")

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request):
    return HttpResponse("Book edit view (requires can_edit permission)")

@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request):
    return HttpResponse("Book delete view (requires can_delete permission)")

