# Generated by Django 2.2 on 2019-11-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='accounts',
            field=models.ManyToManyField(blank=True, to='Accounts.Account'),
        ),
    ]
