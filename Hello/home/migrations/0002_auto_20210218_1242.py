# Generated by Django 3.1.6 on 2021-02-18 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Contact',
            new_name='phone',
        ),
    ]
