# Generated by Django 3.1.1 on 2021-06-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balancer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactions',
            name='pcoe2',
            field=models.IntegerField(default=None),
        ),
    ]
