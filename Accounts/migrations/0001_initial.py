# Generated by Django 2.2 on 2019-11-08 14:48

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accType', models.PositiveSmallIntegerField(choices=[('1', 'Saving'), ('2', 'Insurance')])),
                ('credit', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('surname', models.CharField(default='', max_length=255)),
                ('balance', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('accounts', models.ManyToManyField(to='Accounts.Account')),
            ],
        ),
    ]
