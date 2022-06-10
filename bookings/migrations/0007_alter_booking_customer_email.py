# Generated by Django 3.2 on 2022-06-10 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_rename_default_email_customerprofile_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookings.customerprofile'),
        ),
    ]
