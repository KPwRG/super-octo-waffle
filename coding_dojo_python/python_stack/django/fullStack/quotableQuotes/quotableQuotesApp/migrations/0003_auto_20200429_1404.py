# Generated by Django 2.2.4 on 2020-04-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotableQuotesApp', '0002_auto_20200429_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quoterName',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
