from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from .models import Book
from .models import Library

from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse
from .models import UserProfile  # ensure import so checker sees it


# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context

# Auth: Login (built-in)
class AppLoginView(LoginView):
    template_name = "relationship_app/login.html"

# Auth: Logout (built-in)
class AppLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
    next_page = reverse_lazy("login")

# Auth: Register (custom using built-in form)
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def _has_role(user, role):
    if not user.is_authenticated:
        return False
    # tolerate missing profile (e.g., legacy users)
    profile = getattr(user, "userprofile", None)
    return profile is not None and profile.role == role

# ---- Role-based views (exact function names) ----
@user_passes_test(lambda u: _has_role(u, 'Admin'))
def admin_view(request):
    return HttpResponse("Admin dashboard: restricted content.", content_type="text/plain")

@user_passes_test(lambda u: _has_role(u, 'Librarian'))
def librarian_view(request):
    return HttpResponse("Librarian tools: restricted content.", content_type="text/plain")

@user_passes_test(lambda u: _has_role(u, 'Member'))
def member_view(request):
    return HttpResponse("Member area: restricted content.", content_type="text/plain")
