# Generated by Django 3.2 on 2022-06-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_marketplace', '0009_auto_20220607_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageposts',
            name='slug',
            field=models.SlugField(blank=True, default='name of image', max_length=200, unique=True),
        ),
    ]
