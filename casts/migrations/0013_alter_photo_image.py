# Generated by Django 3.2.7 on 2021-10-05 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casts', '0012_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images/fossils', verbose_name='Image'),
        ),
    ]
