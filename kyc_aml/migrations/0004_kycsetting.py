# Generated by Django 3.1.8 on 2021-08-31 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyc_aml', '0003_auto_20210831_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='KYCSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable_kyc', models.BooleanField(default=True, help_text='Activates or Deactivates KYC application on the system', verbose_name='Enable KYC Verification')),
                ('allow_resubmission', models.BooleanField(default=False, help_text='Allows User to resubmit KYC application if the previous attempt failed. This can only be done a number of times', verbose_name='Allow KYC Re-submission')),
                ('number_of_kyc_tries', models.PositiveIntegerField(default=1, help_text='Number of times a user is allowed to attempt KYC application', verbose_name='Allow KYC tries')),
                ('run_check_on_expiry', models.BooleanField(default=False, help_text="Automated checks to find out if a user's ID has expired", verbose_name='Run check on Expiry')),
                ('days_to_send_notification', models.PositiveIntegerField(default=30, help_text='If run check on expiry is turned on, indicate the number of days which the client receives a reminder of ID expiration and request for re-verification', verbose_name='Verification Notification')),
                ('review_frequency', models.PositiveIntegerField(default=30, help_text='The amount of time on which a User must be reviewed', verbose_name='Review Frequency')),
                ('kyc_system_type', models.CharField(choices=[('manual', 'Manual KYC'), ('automatic', 'Automatic KYC')], default='automatic', help_text='Type of KYC system the User prefers to use', max_length=10, verbose_name='KYC System Type')),
            ],
            options={
                'verbose_name': 'KYC Setting',
                'verbose_name_plural': 'KYC Settings',
            },
        ),
    ]
