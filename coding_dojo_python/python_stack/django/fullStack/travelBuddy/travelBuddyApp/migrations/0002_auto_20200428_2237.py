# Generated by Django 2.2.4 on 2020-04-29 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelBuddyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='travler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travel', to='travelBuddyApp.User'),
        ),
    ]
