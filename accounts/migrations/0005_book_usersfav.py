# Generated by Django 3.0.6 on 2020-05-20 07:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='usersfav',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
