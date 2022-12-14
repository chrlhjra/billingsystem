# Generated by Django 3.1.3 on 2021-08-20 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0080_auto_20210819_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_history',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField(default=0)),
                ('date', models.DateField()),
                ('or_number', models.CharField(max_length=45)),
                ('time', models.CharField(max_length=45)),
                ('podted_by', models.CharField(max_length=45)),
                ('consumer', models.CharField(max_length=45)),
                ('accountinfoid', models.CharField(max_length=45)),
                ('meternumber', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'payment_history',
            },
        ),
    ]
