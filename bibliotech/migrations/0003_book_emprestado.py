# Generated by Django 5.0.7 on 2024-08-12 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotech', '0002_book_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='emprestado',
            field=models.BooleanField(default=False),
        ),
    ]
