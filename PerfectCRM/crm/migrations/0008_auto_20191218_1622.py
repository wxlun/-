# Generated by Django 3.0 on 2019-12-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20191218_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='emergency_contact',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='id_num',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='sex',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, '男'), (1, '女')], null=True),
        ),
    ]
