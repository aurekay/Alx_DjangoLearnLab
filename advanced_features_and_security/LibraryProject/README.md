# Permissions & Groups (bookshelf app)

## Custom Permissions on `bookshelf.Book`
- `can_view`: Can view books
- `can_create`: Can create books
- `can_edit`: Can edit books
- `can_delete`: Can delete books

## Permission-Protected Views (`bookshelf/views.py`)
- `book_list` → requires `bookshelf.can_view`
- `book_create` → requires `bookshelf.can_create`
- `book_edit` → requires `bookshelf.can_edit`
- `book_delete` → requires `bookshelf.can_delete`

## Groups Setup
- **Viewers**: assigned `can_view`
- **Editors**: assigned `can_view`, `can_create`, `can_edit`
- **Admins**: assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)

These groups are configured via Django Admin.

