# Generated by Django 3.0.3 on 2020-04-15 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelrun',
            name='server',
            field=models.BooleanField(null=True),
        ),
    ]
