# Generated by Django 4.1.5 on 2023-03-16 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_alter_orders_phone_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='phone_no',
            new_name='phone',
        ),
    ]
