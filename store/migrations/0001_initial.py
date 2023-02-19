# Generated by Django 4.1.5 on 2023-01-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=100)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]