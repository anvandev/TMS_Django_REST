# Generated by Django 3.1.4 on 2020-12-23 10:09

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=160)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=6)),
            ],
            options={
                'verbose_name': ' Товар ',
                'verbose_name_plural': ' Товары ',
            },
        ),
    ]
