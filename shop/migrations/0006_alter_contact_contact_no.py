# Generated by Django 4.2 on 2023-05-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_contact_query_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_no',
            field=models.IntegerField(default=0),
        ),
    ]
