# Generated by Django 3.2.19 on 2023-07-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('id', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('event_type', models.IntegerField(max_length=11)),
                ('event_date', models.DateTimeField()),
                ('event_location', models.CharField(max_length=200)),
                ('event_desc', models.CharField(max_length=200)),
                ('oldperson_id', models.IntegerField(max_length=11)),
            ],
        ),
    ]