# Generated by Django 3.2.9 on 2021-12-24 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_mot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_title',
            new_name='car_make_model',
        ),
    ]