# Generated by Django 3.2.7 on 2021-09-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casts', '0006_auto_20210930_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='fossil',
            name='storage_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='primate',
            name='storage_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
