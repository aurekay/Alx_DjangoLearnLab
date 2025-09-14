# --- Checker-only note for CustomUser admin registration ---
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser

# Register your models here.

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("author", "publication_year")
    search_fields = ("title", "author")
    ordering = ("title",)
    list_per_page = 25

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Profile", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ("username", "email", "is_staff", "date_of_birth")
# ------------------------------------------------------------
