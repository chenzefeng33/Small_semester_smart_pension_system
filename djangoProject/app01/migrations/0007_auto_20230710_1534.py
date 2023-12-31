# Generated by Django 3.2.19 on 2023-07-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20230704_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='工作人员id'),
        ),
        migrations.AlterField(
            model_name='event_info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='事件id'),
        ),
        migrations.AlterField(
            model_name='oldperson_info',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='老人id'),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='系统管理员id'),
        ),
        migrations.AlterField(
            model_name='volunteer_info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='义工id'),
        ),
    ]
