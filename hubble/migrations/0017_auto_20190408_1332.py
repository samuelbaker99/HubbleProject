# Generated by Django 2.2 on 2019-04-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubble', '0016_auto_20190408_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='auction'),
        ),
    ]
