# Generated by Django 2.2 on 2019-04-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubble', '0012_auto_20190408_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='ftp.jpg', upload_to='media/auction'),
        ),
    ]