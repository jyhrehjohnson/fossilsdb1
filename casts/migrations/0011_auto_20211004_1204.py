# Generated by Django 3.2.7 on 2021-10-04 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casts', '0010_delete_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fossil',
            old_name='storage_location',
            new_name='ut_storage_location',
        ),
        migrations.RenameField(
            model_name='primate',
            old_name='storage_location',
            new_name='ut_storage_location',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='image',
        ),
        migrations.RemoveField(
            model_name='primate',
            name='image',
        ),
    ]
