from datetime import datetime
from ipware import get_client_ip #get's the clients ip address
from crispy_forms.helper import FormHelper 

from django import forms
from django.forms import ValidationError 
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .models import KYCApplication 
from locations.models import Country 

User = settings.AUTH_USER_MODEL 

class DateInput(forms.DateInput):
	input_type = 'date' 

class KYCApplicationForm(forms.ModelForm):

	citizenship = forms.ModelChoiceField(
		queryset=Country.objects.filter(accept_signup=True)) #Only display countries we can accept signup from


	class Meta:
		model = KYCApplication
		exclude = (
			'kyc_status', 'created_date', 'modified_date', 'reviewer'
			'kyc_submitted_ip_address', 'selfie_with_id', 'user'
			'reference', 'date_of_birth', 'number_of_kyc_tries'
			)

	def __init__(self, *args, **kwargs):
		super(KYCApplicationForm, self).__init__(*args, **kwargs)
		self.fields['legal_first_name'].help_text = _("As shown in your documents")
		self.fields['legal_last_name'].help_text = _("As shown in your documents")
		self.fields['politically_exposed_person'].help_text = _("""A politically exposed person(PEP) is one who has been entrusted with 
			a prominent public function. A PEP generally present a higher risk for potential involvement in bribery
			and corruption by virtue of their position and the influence that they may hold. 'not_pep'
			implies the user is not politically exposed and 'pep' implies the user is. """)
		self.fields['country_residence'].help_text = _("The country of residence of the user as shown in documents")
		self.fields['citizenship'].help_text = _("The citizenship of the user as shown in documents")

		#These fields where disabled because they were already provided during signup
		self.fields['country_residence'].disabled = True
		self.fields['legal_first_name'].disabled = True
		self.fields['legal_last_name'].disabled = True
		self.helper = FormHelper()
		self.helper.form_show_labels = False

