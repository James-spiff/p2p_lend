# Generated by Django 3.1.8 on 2021-08-25 16:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='English name of Country', max_length=255, verbose_name='Country Name')),
                ('phone_code', models.CharField(blank=True, help_text='Country code', max_length=100, null=True, verbose_name='Phone Code')),
                ('currency', models.CharField(blank=True, help_text="Country's currency.", max_length=50, null=True, verbose_name='Currency')),
                ('iso2', models.CharField(blank=True, help_text='Two-letter country code.', max_length=2, null=True, verbose_name='ISO2')),
                ('native', models.CharField(blank=True, help_text='Native language of the country.', max_length=255, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='Timestamp of when the record was created.', verbose_name='Date created')),
                ('modified_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='Timestamp of when the record was modified.', verbose_name='Date modified')),
                ('accept_signup', models.BooleanField(default=True, help_text='Allows users from a country to signup.', verbose_name='Accept Signup')),
                ('banned', models.BooleanField(default=False, help_text='Indicates if a country is banned.', verbose_name='Banned Countries')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the State', max_length=255, verbose_name='State Name')),
                ('country_code', models.CharField(blank=True, help_text='The ISO 4217 code of the country', max_length=2, null=True, verbose_name='Country Code')),
                ('iso2', models.CharField(blank=True, help_text='Two-letter state code.', max_length=2, null=True, verbose_name='ISO2')),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='Timestamp of when the record was created.', verbose_name='Date created')),
                ('modified_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='Timestamp of when the record was modified.', verbose_name='Date modified')),
                ('country', models.ForeignKey(help_text='Name of the country for the state', on_delete=django.db.models.deletion.PROTECT, to='locations.country', verbose_name='Country Name')),
            ],
            options={
                'verbose_name': 'State / Region',
                'verbose_name_plural': 'States / Regions',
                'db_table': 'states_regions',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the city location', max_length=255, verbose_name='City Name')),
                ('country_code', models.CharField(blank=True, max_length=2, null=True, verbose_name='Country Code')),
                ('state_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='State Code')),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='Timestamp of when the record was created.', verbose_name='Date created')),
                ('modified_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='Timestamp of when the record was modified.', verbose_name='Date modified')),
                ('country', models.ForeignKey(help_text='Name of the country for the state', on_delete=django.db.models.deletion.PROTECT, to='locations.country', verbose_name='Country Name')),
                ('state', models.ForeignKey(help_text='Name of the state, province or region', on_delete=django.db.models.deletion.PROTECT, to='locations.state', verbose_name='State Name')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'city_locations',
            },
        ),
    ]
