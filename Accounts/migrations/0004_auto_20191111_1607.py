# Generated by Django 2.2.7 on 2019-11-11 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20191108_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='accounts',
            field=models.ManyToManyField(blank=True, related_name='account_list', to='Accounts.Account'),
        ),
    ]