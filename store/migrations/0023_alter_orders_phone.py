# Generated by Django 4.1.5 on 2023-03-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_alter_orders_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
