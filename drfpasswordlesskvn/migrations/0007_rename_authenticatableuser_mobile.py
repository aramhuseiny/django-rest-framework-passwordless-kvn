# Generated by Django 4.1.5 on 2023-01-15 14:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drfpasswordlesskvn', '0006_authenticatableuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuthenticatableUser',
            new_name='Mobile',
        ),
    ]
