# Generated by Django 3.0 on 2019-12-18 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20191218_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentenrollment',
            name='class_grade',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList'),
        ),
        migrations.AlterField(
            model_name='studentenrollment',
            name='customer',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='crm.CustomerInfo'),
        ),
    ]