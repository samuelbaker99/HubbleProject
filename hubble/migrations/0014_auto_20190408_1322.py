# Generated by Django 2.2 on 2019-04-08 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubble', '0013_auto_20190408_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='null', upload_to='media/auction'),
        ),
    ]