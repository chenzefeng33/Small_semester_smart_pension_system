# Generated by Django 3.2.19 on 2023-07-03 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinfo',
            name='test',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='eventinfo',
            name='event_type',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='eventinfo',
            name='id',
            field=models.IntegerField(default=0, max_length=11, primary_key=True, serialize=False),
        ),
    ]
