# Generated by Django 3.1.3 on 2021-10-12 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0084_auto_20210921_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_info',
            name='duedate',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='consumers_info',
            name='birthday',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='consumers_info',
            name='middlename',
            field=models.CharField(default='', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='consumers_info',
            name='mobilenumber2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consumers_info',
            name='sitio',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
