# Generated by Django 3.1.8 on 2021-08-31 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyc_aml', '0004_kycsetting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kycapplication',
            name='agreed_to_data_usage',
            field=models.BooleanField(default=False, help_text='Agreement collected from the user to gain consent to use their provided data', verbose_name='Agree to data usage'),
        ),
    ]