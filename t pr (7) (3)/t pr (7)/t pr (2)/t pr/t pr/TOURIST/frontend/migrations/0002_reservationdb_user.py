# Generated by Django 4.2.2 on 2023-06-20 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationdb',
            name='user',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
