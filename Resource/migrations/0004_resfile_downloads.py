# Generated by Django 2.1.7 on 2019-05-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0003_auto_20190424_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='resfile',
            name='downloads',
            field=models.IntegerField(default=0),
        ),
    ]