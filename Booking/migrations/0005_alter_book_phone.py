# Generated by Django 5.0.4 on 2024-05-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0004_book_name_book_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]