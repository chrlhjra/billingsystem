# Generated by Django 3.1.3 on 2021-04-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0024_usage_record_accountinfoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usage_record',
            name='datepaid_mar',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]
