# Generated by Django 4.2.2 on 2023-06-20 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_remove_productdb_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdb',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='productdb',
            name='name',
        ),
        migrations.RemoveField(
            model_name='productdb',
            name='traveldate',
        ),
    ]
