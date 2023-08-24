# Generated by Django 4.2 on 2023-05-25 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_contact_contact_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=10)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
    ]