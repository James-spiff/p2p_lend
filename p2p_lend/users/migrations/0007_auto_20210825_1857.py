# Generated by Django 3.1.8 on 2021-08-25 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('users', '0006_auto_20210805_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country_of_residence',
            field=models.ForeignKey(blank=True, help_text="Client's country of residence. KYC verification will be applied to this country with proof of residence.", null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.country', verbose_name='Country of Residence'),
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of the instance this object belongs to.\n                    Mandatory, unless a new instance to create is given.', primary_key=True, serialize=False)),
                ('address_line_1', models.CharField(help_text='Adress line 1 of the user', max_length=125, verbose_name='Adress line 1')),
                ('address_line_2', models.CharField(blank=True, help_text='Adress line 2 of the user', max_length=125, null=True, verbose_name='Adress line 2')),
                ('zip_post_code', models.CharField(help_text='User zip code', max_length=20, verbose_name='Zip code')),
                ('city', models.ForeignKey(help_text='City of residence', on_delete=django.db.models.deletion.PROTECT, to='locations.city', verbose_name='City')),
                ('country', models.ForeignKey(help_text='Country of residence', on_delete=django.db.models.deletion.PROTECT, to='locations.country', verbose_name='Country')),
                ('state', models.ForeignKey(help_text='State of residence', on_delete=django.db.models.deletion.PROTECT, to='locations.state', verbose_name='State')),
                ('user', models.ForeignKey(help_text='The user that owns the adress', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Adress',
                'verbose_name_plural': 'User Adresses',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='current_adress',
            field=models.ForeignKey(blank=True, help_text='Current adress of the client.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='users.useraddress', verbose_name='Current Adress'),
        ),
        migrations.AlterField(
            model_name='user',
            name='permanent_adress',
            field=models.ForeignKey(blank=True, help_text='Permanent adress of the client.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='users.useraddress', verbose_name='Permanent Adress'),
        ),
    ]
