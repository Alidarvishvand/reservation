# Generated by Django 3.2.20 on 2024-08-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
