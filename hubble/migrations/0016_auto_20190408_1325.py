# Generated by Django 2.2 on 2019-04-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubble', '0015_auto_20190408_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='', upload_to='auction'),
        ),
    ]