# Django Permissions and Groups Setup

This Django project demonstrates the use of custom permissions and groups to control access to various parts of the application.

## Custom Permissions
- `can_view`: Permission to view a book.
- `can_create`: Permission to create a book.
- `can_edit`: Permission to edit a book.
- `can_delete`: Permission to delete a book.

## Groups and Permissions
- **Editors**: Can view, create, and edit books.
- **Viewers**: Can only view books.
- **Admins**: Can view, create, edit, and delete books.

## Setting Up Groups and Permissions
- Groups and permissions are created automatically during migration.
- You can assign users to these groups via the Django admin interface or the Django shell.

## Views
Permissions are enforced using the `@permission_required` decorator. Users must have the required permissions to access certain views.
