# Generated by Django 3.2.5 on 2021-07-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightdata',
            name='pub_date',
            field=models.CharField(max_length=200),
        ),
    ]
