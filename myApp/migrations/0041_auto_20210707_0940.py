# Generated by Django 3.1.3 on 2021-07-07 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0040_auto_20210706_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gettotalbill',
            name='previous_reading',
        ),
        migrations.RemoveField(
            model_name='gettotalbill',
            name='reading_date',
        ),
        migrations.AddField(
            model_name='revenuecode',
            name='disconnection_after',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='revenuecode',
            name='send_disconnection_notice_after',
            field=models.IntegerField(default=0),
        ),
    ]
