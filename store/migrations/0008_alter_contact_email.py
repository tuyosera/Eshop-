# Generated by Django 4.1.5 on 2023-01-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='name@gmail.com', max_length=30),
        ),
    ]
