# Generated by Django 3.2.5 on 2021-07-24 03:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weightdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 7, 24, 3, 42, 19, 517447, tzinfo=utc))),
                ('uuid', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
