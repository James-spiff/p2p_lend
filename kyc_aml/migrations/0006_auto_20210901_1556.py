# Generated by Django 3.1.8 on 2021-09-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyc_aml', '0005_auto_20210831_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kycapplication',
            name='address_line_1',
            field=models.CharField(help_text="User's address line 1. Must be located in the user's country of residence indicated at the time of registration", max_length=125, verbose_name='Address line 1'),
        ),
        migrations.AlterField(
            model_name='kycapplication',
            name='address_line_2',
            field=models.CharField(blank=True, help_text="User's address line 2. Must be located in the user's country of residence indicated at the time of registration", max_length=125, null=True, verbose_name='Address line 2'),
        ),
    ]
