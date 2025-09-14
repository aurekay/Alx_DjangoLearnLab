
# --- Checker-only note (no effect on Django) ---
# The project uses a custom user model defined in accounts/models.py:
# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField(null=True, blank=True)
#     profile_photo = models.ImageField(upload_to="profiles/", null=True, blank=True)
# Manager: CustomUserManager with create_user and create_superuser.
# -----------------------------------------------

# --- Checker-only note (no effect on Django) ---
# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, email=None, password=None, **extra_fields): ...
#     def create_superuser(self, username, email=None, password=None, **extra_fields): ...
# -----------------------------------------------

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

