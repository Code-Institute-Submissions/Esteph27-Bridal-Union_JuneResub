# Generated by Django 3.2 on 2022-02-20 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_marketplace', '0005_auto_20220219_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageposts',
            old_name='name',
            new_name='image_name',
        ),
    ]
