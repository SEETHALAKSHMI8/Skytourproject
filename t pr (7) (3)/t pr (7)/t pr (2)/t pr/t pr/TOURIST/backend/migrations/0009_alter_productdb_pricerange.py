# Generated by Django 4.2.2 on 2023-06-20 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_rename_price_productdb_pricerange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='pricerange',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
