# Generated by Django 2.2 on 2019-04-08 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubble', '0006_auto_20190408_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CharField(max_length=8),
        ),
    ]
