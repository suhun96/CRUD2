# Generated by Django 4.0.3 on 2022-03-15 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_author', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='authorbook',
            table='authorsbooks',
        ),
        migrations.AlterModelTable(
            name='book',
            table='books',
        ),
    ]