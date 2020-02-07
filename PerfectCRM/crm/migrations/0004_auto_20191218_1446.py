# Generated by Django 3.0 on 2019-12-18 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20191209_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('content', models.CharField(max_length=64)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='customerinfo',
            options={'verbose_name': '客户信息', 'verbose_name_plural': '客户信息'},
        ),
        migrations.AlterField(
            model_name='student',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.CustomerInfo'),
        ),
        migrations.CreateModel(
            name='StudentEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_agreed', models.BooleanField(default=False)),
                ('contract_signed_date', models.DateTimeField(blank=True, null=True)),
                ('contract_approved', models.BooleanField(default=False)),
                ('contract_approved_date', models.DateTimeField(blank=True, null=True, verbose_name='合同审核时间')),
                ('class_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.CustomerInfo')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.SmallIntegerField(choices=[(0, '报名费'), (1, '学费'), (2, '退费')], default=0)),
                ('amount', models.IntegerField(default=500, verbose_name='学费')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.StudentEnrollment')),
            ],
        ),
        migrations.AddField(
            model_name='classlist',
            name='contract_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.ContractTemplate'),
        ),
    ]