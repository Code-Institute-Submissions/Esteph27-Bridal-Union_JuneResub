# Generated by Django 3.2 on 2022-06-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_marketplace', '0008_imageposts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageposts',
            name='image_name',
            field=models.CharField(default='name of image', max_length=200),
        ),
        migrations.AlterField(
            model_name='imageposts',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]