# Generated by Django 4.0.4 on 2022-05-17 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_rename_hotels_review_hotel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='users',
            new_name='user',
        ),
    ]
