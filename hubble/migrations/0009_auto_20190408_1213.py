# Generated by Django 2.2 on 2019-04-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubble', '0008_auto_20190408_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='auction'),
        ),
    ]
