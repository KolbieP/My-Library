# Generated by Django 4.2.5 on 2025-04-16 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookListAPI', '0005_publicbook'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PublicBook',
        ),
    ]
