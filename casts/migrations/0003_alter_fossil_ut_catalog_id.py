# Generated by Django 3.2.7 on 2021-09-29 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casts', '0002_auto_20210929_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fossil',
            name='ut_catalog_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
