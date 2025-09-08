from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, permission_required

from .models import Book
from .models import Library
from .models import Author
from .models import UserProfile

# -------------------------------
# Function-based view: list books
# -------------------------------
def list_books(request):
    books = Book.objects.select_related("author").all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# -------------------------------
# Class-based view: library detail
# -------------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.select_related("author").all()
        return context

# -------------------------------
# Authentication views
# -------------------------------
class AppLoginView(LoginView):
    template_name = "relationship_app/login.html"

class AppLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
    next_page = reverse_lazy("login")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# -------------------------------
# Role-Based Access Control (RBAC)
# -------------------------------
def _has_role(user, role):
    profile = getattr(user, "userprofile", None)
    return user.is_authenticated and profile and profile.role == role

@user_passes_test(lambda u: _has_role(u, "Admin"))
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(lambda u: _has_role(u, "Librarian"))
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(lambda u: _has_role(u, "Member"))
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# -------------------------------
# Custom-permission protected CRUD
# -------------------------------
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    """
    Accepts POST with 'title' and 'author_name'.
    """
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author_name = request.POST.get("author_name", "").strip()
        if not title or not author_name:
            return HttpResponse("Missing 'title' or 'author_name'.", status=400)
        author, _ = Author.objects.get_or_create(name=author_name)
        Book.objects.create(title=title, author=author)
        return redirect("list_books")
    # Simple inline form to avoid extra templates
    return HttpResponse(
        "<h1>Add Book</h1>"
        "<form method='post'>"
        "{% csrf_token %}"
        "Title: <input name='title'><br>"
        "Author name: <input name='author_name'><br>"
        "<button type='submit'>Save</button>"
        "</form>"
    )

@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, pk: int):
    """
    Accepts POST with 'title' and 'author_name' to update.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author_name = request.POST.get("author_name", "").strip()
        if not title or not author_name:
            return HttpResponse("Missing 'title' or 'author_name'.", status=400)
        author, _ = Author.objects.get_or_create(name=author_name)
        book.title = title
        book.author = author
        book.save()
        return redirect("list_books")
    return HttpResponse(
        f"<h1>Edit Book #{book.pk}</h1>"
        "<form method='post'>"
        "{% csrf_token %}"
        f"Title: <input name='title' value='{book.title}'><br>"
        f"Author name: <input name='author_name' value='{book.author.name}'><br>"
        "<button type='submit'>Update</button>"
        "</form>"
    )

@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, pk: int):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return HttpResponse(
        f"<h1>Delete Book #{book.pk}</h1>"
        f"<p>Are you sure you want to delete '{book.title}'?</p>"
        "<form method='post'>"
        "{% csrf_token %}"
        "<button type='submit'>Confirm delete</button>"
        "</form>"
    )

