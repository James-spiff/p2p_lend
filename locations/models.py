from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

"""Below are the models for Country, State and City"""

# Represents a country
class Country(models.Model):
	#region fields
	name = models.CharField(
		max_length=255,
		verbose_name=_('Country Name'),
		help_text=_('English name of Country'))

	phone_code = models.CharField(
		max_length=100,
		blank=True, null=True,
		verbose_name=_('Phone Code'),
		help_text=_('Country code'))

	currency = models.CharField(
		max_length=50,
		blank=True, null=True,
		verbose_name=_('Currency'),
		help_text=_("Country's currency."))

	# iso3 = models.CharField(
	# 	max_length=3,
	# 	blank=True, null=True,
	# 	verbose_name=_('ISO3'),
	# 	help_text=_('Three-letter country code'))

	iso2 = models.CharField(
		max_length=2,
		blank=True, null=True,
		verbose_name=_('ISO2'),
		help_text=_('Two-letter country code.'))

	# capital = models.CharField(
	# 	max_length=255,
	# 	blank=True, null=True,
	# 	verbose_name=_('Capital'),
	# 	help_text=_('Capital of country'))

	native = models.CharField(
		max_length=255,
		blank=True, null=True,
		help_text=_('Native language of the country.'))

	# region = models.CharField(
	# 	max_length=255,
	# 	blank=True, null=True,
	# 	verbose_name=_('Region'),
	# 	help_text=_('Region of the country'))

	created_date = models.DateTimeField(
		default=timezone.now,
		blank=True, editable=False,
		verbose_name=_('Date created'),
		help_text=_('Timestamp of when the record was created.'))

	modified_date = models.DateTimeField(
		default=timezone.now,
		blank=True, editable=False,
		verbose_name=_('Date modified'),
		help_text=_('Timestamp of when the record was modified.'))

	#This checks if users from a specific country are alloed to signup
	accept_signup = models.BooleanField(
		default=True,
		verbose_name=_('Accept Signup'),
		help_text=_('Allows users from a country to signup.'))

	banned = models.BooleanField(
		default=False,
		verbose_name=_('Banned Countries'),
		help_text=_('Indicates if a country is banned.'))

	class Meta:
		verbose_name = _('Country')
		verbose_name_plural = _('Countries')
		db_table = 'countries'

	def __str__(self):
		return self.name 

class State(models.Model):

	name = models.CharField(
		max_length=255,
		verbose_name=_('State Name'),
		help_text=_('Name of the State'))

	#ISO code for the country the state is located in
	country_code = models.CharField(
		max_length=2,
		blank=True, null=True,
		verbose_name=_('Country Code'),
		help_text=_('The ISO 4217 code of the country'))

	iso2 = models.CharField(
		max_length=2,
		blank=True, null=True,
		verbose_name=_('ISO2'),
		help_text=_('Two-letter state code.'))

	created_date = models.DateTimeField(
		default=timezone.now,
		blank=True, editable=False,
		verbose_name=_('Date created'),
		help_text=_('Timestamp of when the record was created.'))

	modified_date = models.DateTimeField(
		default=timezone.now,
		blank=True, editable=False,
		verbose_name=_('Date modified'),
		help_text=_('Timestamp of when the record was modified.'))

	#Foreign key
	country = models.ForeignKey(
		Country,
		on_delete=models.PROTECT,
		verbose_name=_('Country Name'),
		help_text=_('Name of the country for the state'))

	class Meta:
		verbose_name = _('State / Region')
		verbose_name_plural = _('States / Regions')
		db_table = 'states_regions'

	def __str__(self):
		return self.name


class City(models.Model):
	"""Holds cities and location data of countries around the world"""

	name = models.CharField(
		max_length=255,
		verbose_name=_('City Name'),
		help_text=_('Name of the city location'))

	country_code = models.CharField(
		max_length=2,
		blank=True, null=True,
		verbose_name=_('Country Code'))

	state_code = models.CharField(
		max_length=5,
		blank=True, null=True,
		verbose_name=_('State Code'))

	created_date = models.DateTimeField(
		default=timezone.now,
		blank=True, editable=False,
		verbose_name=_('Date created'),
		help_text=_('Timestamp of when the record was created.'))

	modified_date = models.DateTimeField(
		default=timezone.now,
		blank=True, editable=False,
		verbose_name=_('Date modified'),
		help_text=_('Timestamp of when the record was modified.'))

	#Foreign keys
	country = models.ForeignKey(
		Country,
		on_delete=models.PROTECT,
		verbose_name=_('Country Name'),
		help_text=_('Name of the country for the state'))

	state = models.ForeignKey(
		State,
		on_delete=models.PROTECT,
		verbose_name=_('State Name'),
		help_text=_('Name of the state, province or region'))

	class Meta:
		verbose_name = _('City')
		verbose_name_plural = _('Cities')
		db_table = 'city_locations'

	def __str__(self):
		return self.name