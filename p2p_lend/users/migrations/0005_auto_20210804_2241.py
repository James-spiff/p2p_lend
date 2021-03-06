# Generated by Django 3.1.13 on 2021-08-04 21:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210418_1932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Register User', 'verbose_name_plural': 'Registered Users'},
        ),
        migrations.AddField(
            model_name='user',
            name='contact_number',
            field=models.CharField(blank=True, help_text='Contact number of the client.', max_length=50, null=True, verbose_name='Contact Number'),
        ),
        migrations.AddField(
            model_name='user',
            name='country_of_residence',
            field=models.CharField(blank=True, help_text="Client's country of residence. KYC verification will be applied to this country with proof of residence.", max_length=125, null=True, verbose_name='Country of Residence'),
        ),
        migrations.AddField(
            model_name='user',
            name='current_adress',
            field=models.CharField(blank=True, help_text='Current adress of the client.', max_length=225, null=True, verbose_name='Current Adress'),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text="Client's date of birth.", null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='user',
            name='default_currency',
            field=models.CharField(blank=True, default='EUR', help_text='Default currency of the borrower.', max_length=3, null=True, verbose_name='Default Currency'),
        ),
        migrations.AddField(
            model_name='user',
            name='job_title',
            field=models.CharField(blank=True, help_text="Client's job title.", max_length=125, null=True, verbose_name='Job Title'),
        ),
        migrations.AddField(
            model_name='user',
            name='kyc_complete',
            field=models.BooleanField(default=False, help_text='Flag to determine if customer has completed KYC verification.', verbose_name='KYC Complete'),
        ),
        migrations.AddField(
            model_name='user',
            name='kyc_complete_date',
            field=models.DateTimeField(blank=True, help_text='Timestamp for KYC verification.', null=True, verbose_name='KYC Completion Date'),
        ),
        migrations.AddField(
            model_name='user',
            name='kyc_status',
            field=models.CharField(blank=True, choices=[('unverified', 'Unverified'), ('pending', 'Pending'), ('verified', 'Verified'), ('action_required', 'Action Required'), ('cancelled', 'Cancelled'), ('rejected', 'Rejected')], default='Unverified', help_text='KYC status of the client.', max_length=15, null=True, verbose_name='KYC Status'),
        ),
        migrations.AddField(
            model_name='user',
            name='kyc_submitted',
            field=models.BooleanField(default=False, help_text='Flag to determine if customer has submitted their KYC.', verbose_name='KYC Submitted'),
        ),
        migrations.AddField(
            model_name='user',
            name='onboarding_complete',
            field=models.BooleanField(default=False, help_text='Flag to determine if customer has completed onboarding.', verbose_name='Completed Onboarding'),
        ),
        migrations.AddField(
            model_name='user',
            name='onboarding_complete_date',
            field=models.DateTimeField(blank=True, help_text='Timestamp for onboarding completion.', null=True, verbose_name='Onboarding Completion Date'),
        ),
        migrations.AddField(
            model_name='user',
            name='permanent_adress',
            field=models.CharField(blank=True, help_text='Permanent adress of the client.', max_length=225, null=True, verbose_name='Permanent Adress'),
        ),
        migrations.AddField(
            model_name='user',
            name='place_of_birth',
            field=models.CharField(blank=True, help_text="Client's place of birth.", max_length=150, null=True, verbose_name='Place of Birth'),
        ),
        migrations.AddField(
            model_name='user',
            name='registered_ip_address',
            field=models.GenericIPAddressField(blank=True, editable=False, help_text="Client's ip address recorded at the time of registration.", null=True, verbose_name='Registered IP Address'),
        ),
        migrations.AddField(
            model_name='user',
            name='social_security_number',
            field=models.CharField(blank=True, help_text='Social security number of the client.', max_length=50, null=True, verbose_name='Social Security Number'),
        ),
        migrations.AddField(
            model_name='user',
            name='verification_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text="Timestamp when client's profile was verified.", null=True, verbose_name='Verification Date'),
        ),
    ]
