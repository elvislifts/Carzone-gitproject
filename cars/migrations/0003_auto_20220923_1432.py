# Generated by Django 3.0.7 on 2022-09-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20220923_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[('2', '2'), ('3', '3'), ('4', '4')]),
        ),
    ]
