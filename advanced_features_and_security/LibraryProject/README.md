
# Permissions & Groups (bookshelf app)

Custom permissions on `bookshelf.Book`:
- `can_view`, `can_create`, `can_edit`, `can_delete`

Views (example) protected with `permission_required` in `LibraryProject/bookshelf/views.py`:
- `bookshelf.can_view`, `bookshelf.can_create`, `bookshelf.can_edit`, `bookshelf.can_delete`

Example groups:
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: can_view, can_create, can_edit, can_delete
