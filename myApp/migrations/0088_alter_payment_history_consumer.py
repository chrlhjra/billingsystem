# Generated by Django 3.2.9 on 2022-01-07 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0087_alter_payment_history_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_history',
            name='consumer',
            field=models.CharField(max_length=120),
        ),
    ]
