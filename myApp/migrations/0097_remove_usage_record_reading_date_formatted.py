# Generated by Django 4.1.1 on 2022-09-13 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0096_rename_reading_date_apr_formatted_usage_record_reading_date_formatted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usage_record',
            name='reading_date_formatted',
        ),
    ]