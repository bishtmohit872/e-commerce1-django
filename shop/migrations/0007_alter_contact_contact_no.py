# Generated by Django 4.2 on 2023-05-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_contact_contact_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_no',
            field=models.CharField(default='', max_length=12),
        ),
    ]
