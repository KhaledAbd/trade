# Generated by Django 2.0.5 on 2018-07-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triko', '0013_auto_20180703_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='name',
            field=models.CharField(default='غير موجود', max_length=20),
        ),
        migrations.AddField(
            model_name='triko_model',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
