# Generated by Django 4.1.5 on 2023-03-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(blank=True, default=1, max_length=50, null=True),
        ),
    ]
