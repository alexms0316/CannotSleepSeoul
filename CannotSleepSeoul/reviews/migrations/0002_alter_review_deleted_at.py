# Generated by Django 4.0.4 on 2022-05-17 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
