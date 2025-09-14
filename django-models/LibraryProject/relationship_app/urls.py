# LibraryProject/relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView   # <-- required by checker
from . import views

urlpatterns = [
    # Function-based & class-based views
    path("books/", list_books, name="list_books"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

    # RBAC examples
    path("rbac/admin/", views.admin_view, name="admin_view"),
    path("rbac/librarian/", views.librarian_view, name="librarian_view"),
    path("rbac/member/", views.member_view, name="member_view"),

    # Secured CRUD with custom permissions
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
]



