# Generated by Django 2.2.10 on 2020-06-03 17:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0059_custom_pv_wind_prodfactors'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialmodel',
            name='owner_discount_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='financialmodel',
            name='owner_tax_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='financialmodel',
            name='two_party_ownership',
            field=models.BooleanField(default=False),
        )
    ]