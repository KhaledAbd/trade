# Generated by Django 2.0.5 on 2018-06-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Triko_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('size', models.CharField(choices=[('sm', 'small'), ('md', 'meduim'), ('lg', 'large')], max_length=2)),
                ('image', models.ImageField(upload_to='media/image')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
