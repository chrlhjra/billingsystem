# Generated by Django 3.1.3 on 2021-07-15 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0050_auto_20210715_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemuser',
            name='password',
            field=models.BinaryField(max_length=1000),
        ),
    ]
