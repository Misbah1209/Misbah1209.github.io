# Generated by Django 2.1.5 on 2023-03-17 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20230314_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
