# bookshelf/apps.py

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission

class BookshelfConfig(AppConfig):
    name = 'bookshelf'

    def ready(self):
        # Set up groups and permissions after migration
        post_migrate.connect(self.create_groups_and_permissions, sender=self)

    def create_groups_and_permissions(self, sender, **kwargs):
        # Create or get groups
        editors, created = Group.objects.get_or_create(name='Editors')
        viewers, created = Group.objects.get_or_create(name='Viewers')
        admins, created = Group.objects.get_or_create(name='Admins')

        # Assign custom permissions to groups
        can_view = Permission.objects.get(codename='can_view')
        can_create = Permission.objects.get(codename='can_create')
        can_edit = Permission.objects.get(codename='can_edit')
        can_delete = Permission.objects.get(codename='can_delete')

        # Add permissions to groups
        editors.permissions.add(can_view, can_create, can_edit)
        viewers.permissions.add(can_view)
        admins.permissions.add(can_view, can_create, can_edit, can_delete)
