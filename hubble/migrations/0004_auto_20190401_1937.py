# Generated by Django 2.1.7 on 2019-04-01 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubble', '0003_auto_20190401_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='desc',
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='', max_length=200),
        ),
    ]
