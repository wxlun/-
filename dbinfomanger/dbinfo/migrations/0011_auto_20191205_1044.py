# Generated by Django 3.0 on 2019-12-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbinfo', '0010_auto_20191205_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbmongodbcls',
            name='alytip',
            field=models.CharField(max_length=32, verbose_name='aly同步ip'),
        ),
        migrations.AlterField(
            model_name='dbmongodbcls',
            name='idctip',
            field=models.CharField(max_length=32, verbose_name='IDC同步ip'),
        ),
    ]
