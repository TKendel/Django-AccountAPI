# Generated by Django 2.2.7 on 2019-11-12 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_auto_20191112_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='Accounts.Customer'),
        ),
    ]
