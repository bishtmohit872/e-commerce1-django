# Generated by Django 4.2.1 on 2023-06-13 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_orders_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=20)),
                ('user_email', models.CharField(default='', max_length=20)),
                ('user_password', models.CharField(default='', max_length=15)),
            ],
        ),
    ]