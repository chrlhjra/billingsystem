# Generated by Django 3.1.3 on 2021-08-12 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0073_auto_20210811_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterreadingmodification',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
