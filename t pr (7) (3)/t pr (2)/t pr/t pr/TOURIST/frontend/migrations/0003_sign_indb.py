# Generated by Django 4.2.2 on 2023-06-20 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_reservationdb_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='sign_indb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('cpassword', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]