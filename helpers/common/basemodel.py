from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone

#Creating an abstract model
#All our new models can inherit these fields instead of creating them any time we make new models
class BaseModel(models.Model):

	id = models.UUIDField(
		default=uuid.uuid4,
		editable=False,
		primary_key=True
		)

	created_date = models.DateTimeField(
		verbose_name=_('Date created'),
		default=timezone.now,
		help_text=_('Timestamp when the record was created')
		)

	modified_date = models.DateTimeField(
		verbose_name=_('Date Modified'),
		default=timezone.now,
		help_text=_('Timestamp when the record was modified')
		)


	class Meta:
		abstract=True