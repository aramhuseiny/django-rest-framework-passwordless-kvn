# Generated by Django 4.1.5 on 2023-01-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfpasswordlesskvn', '0007_rename_authenticatableuser_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='mobile',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]