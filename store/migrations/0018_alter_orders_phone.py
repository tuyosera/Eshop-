# Generated by Django 4.1.5 on 2023-03-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_orders_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
