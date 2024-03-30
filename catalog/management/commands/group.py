from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Создание группы модератор
        employee_group = Group.objects.create(name='модератор')
        # Добавление прав доступа
        view_permissions = Permission.objects.filter(codename='view_product')
        set_published_permissions = Permission.objects.filter(codename='set_published')

        employee_group.permissions.set(view_permissions.union(set_published_permissions))

        # Создание аккаунта модератора

        user = User.objects.create(
            email='moderator_admin@mail.ru',
            first_name='Admin',
            last_name='Project',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('moderator3000')
        user.groups.add(employee_group)
        user.save()

