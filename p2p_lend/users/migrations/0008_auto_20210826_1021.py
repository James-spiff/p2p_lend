# Generated by Django 3.1.8 on 2021-08-26 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210825_1857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraddress',
            options={'verbose_name': 'User address', 'verbose_name_plural': 'User addresses'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='current_adress',
        ),
        migrations.RemoveField(
            model_name='user',
            name='permanent_adress',
        ),
        migrations.AddField(
            model_name='user',
            name='current_address',
            field=models.ForeignKey(blank=True, help_text='Current address of the client.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='users.useraddress', verbose_name='Current address'),
        ),
        migrations.AddField(
            model_name='user',
            name='permanent_address',
            field=models.ForeignKey(blank=True, help_text='Permanent address of the client.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='users.useraddress', verbose_name='Permanent address'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='type',
            field=models.CharField(choices=[('current', 'Current Address'), ('permanent', 'Permanent Address')], default='current', help_text='The type of address', max_length=10, verbose_name='Address type'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='address_line_1',
            field=models.CharField(help_text='address line 1 of the user', max_length=125, verbose_name='address line 1'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='address_line_2',
            field=models.CharField(blank=True, help_text='address line 2 of the user', max_length=125, null=True, verbose_name='address line 2'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(help_text='The user that owns the address', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
