# Generated by Django 3.1.3 on 2021-04-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0025_auto_20210420_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarykey_basis',
            name='lastid_used',
            field=models.BigIntegerField(),
        ),
    ]
