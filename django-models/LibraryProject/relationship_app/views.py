from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test

from .models import Book
from .models import Library
from .models import UserProfile


# -------------------------------
# Function-based view: list books
# -------------------------------
def list_books(request):
    books = Book.objects.all()
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
        context["books"] = self.object.books.all()
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
            # log user in immediately after registration
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

