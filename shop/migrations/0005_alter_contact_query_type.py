# Generated by Django 4.2 on 2023-05-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='query_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]