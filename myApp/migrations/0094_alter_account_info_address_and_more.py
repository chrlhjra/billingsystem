# Generated by Django 4.0.5 on 2022-07-09 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0093_account_info_stop_meter_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_info',
            name='address',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='consumers_info',
            name='homeaddress',
            field=models.CharField(max_length=120),
        ),
    ]
