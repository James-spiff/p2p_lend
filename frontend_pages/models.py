from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class TeamMember(models.Model):

	name = models.CharField(
		max_length=125,
		help_text=_('The name of the team member'),
		verbose_name=_('Name')
		)

	designation = models.CharField(
		max_length=125,
		help_text=_('Designation/Position of the team member'),
		verbose_name=_('Designation')
		)

	linkedin = models.URLField(
		max_length=225,
		blank=True, null=True,
		help_text=_('LinkedIn URL'),
		verbose_name=_('LinkedIn handle')
		)


	class Meta:
		verbose_name='Team Member'
		verbose_name_plural='Team Members'


	def __str__(self):
		return self.name