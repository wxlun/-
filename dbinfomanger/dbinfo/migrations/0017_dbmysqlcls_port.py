# Generated by Django 3.0 on 2019-12-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbinfo', '0016_auto_20191205_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbmysqlcls',
            name='port',
            field=models.IntegerField(db_index=True, default='123', max_length=10, verbose_name='端口'),
        ),
    ]
