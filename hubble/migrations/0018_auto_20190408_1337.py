# Generated by Django 2.2 on 2019-04-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubble', '0017_auto_20190408_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='auction'),
        ),
    ]
