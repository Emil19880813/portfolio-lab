# Generated by Django 3.0.5 on 2020-05-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0004_donation_date_of_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='pick_up_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='pick_up_time',
            field=models.TimeField(blank=True),
        ),
    ]
