from django.db import models
from helpers.common.basemodel import BaseModel
from helpers.common.choices import ModelChoices
from django.utils.translation import gettext_lazy as _
from p2p_lend.users.models import User, UserAddress
from locations.models import Country, State, City
from django.utils import timezone
from datetime import datetime
from solo.models import SingletonModel



class KYCApplication(BaseModel):

	legal_first_name = models.CharField(
		max_length=225,
		verbose_name=_('Legal first name'),
		blank=True, null=True,
		help_text=_("User's first name as shown in documents")
		)

	legal_last_name = models.CharField(
		max_length=225,
		verbose_name=_('Legal last name'),
		blank=True, null=True,
		help_text=_("User's last name as shown in documents")
		)

	date_of_birth = models.DateField(
		verbose_name=_('Date of birth'),
		blank=True, null=True,
		help_text=("User's date of birth as shown in documents"))

	email = models.EmailField(
		max_length=150,
		verbose_name=_('Email Address'),
		blank=True,
		help_text=_("User's primary email address"))

	address_line_1 = models.ForeignKey(
		UserAddress,
		on_delete=models.PROTECT,
		verbose_name=_('Address line 1'),
		help_text=_("User's address line 1. Must be located in the user's country of residence indicated at the time of registration")
		)

	address_line_2 = models.ForeignKey(
		UserAddress,
		on_delete=models.PROTECT,
		verbose_name=_('Address line 2'),
		blank=True, null=True,
		related_name='+',
		help_text=_("User's address line 2. Must be located in the user's country of residence indicated at the time of registration")
		)

	state = models.ForeignKey(
		State,
		on_delete=models.PROTECT,
		verbose_name=_('State/Region'),
		help_text=_("User's state of residence. Must be located in the user's country of residence indicated at the time of registration"))

	city = models.ForeignKey(
		City,
		on_delete=models.PROTECT,
		verbose_name=_('City'),
		help_text=_("User's city of residence. Must be located in the user's country of residence indicated at the time of registration"))

	zip_post_code = models.CharField(
		max_length=20,
		verbose_name=_('Zip code'),
		help_text=_('User zip code'))

	identification_type = models.CharField(
		max_length=21,
		verbose_name=_('Indentification Type'),
		choices=ModelChoices.PHOTO_IDENTIFICATION_TYPE,
		default='national_id',
		help_text=_("User's type of identification document to prove their identity"))

	address_proof_type = models.CharField(
 		max_length=21,
 		verbose_name=_('Address proof type'),
 		choices=ModelChoices.PROOF_OF_ADDRESS_TYPE,
 		default=ModelChoices.BANK_STATEMENT,
 		help_text=_("User's type of document to prove his address"))

	proof_of_address_document = models.FileField(
 		storage="uploads/kyc/",
 		verbose_name=_('Proof of address document'),
 		# validators=[validate_kyc_file], #a validator raises a ValidationError if it doesn't meet a specified criteria 
 		help_text=_("The user's document that shows his proof of address. It should not be older than 90 days, expired and must have the user's details written on it."))

	photo_id = models.FileField(
 		storage="uploads/kyc/",
 		verbose_name=_('Photo ID(front)'),
 		# validators=[validate_kyc_file], #a validator raises a ValidationError if it doesn't meet a specified criteria 
 		help_text=_("The front part of the user's valid photo id"))

	photo_id_back = models.FileField(
 		storage="uploads/kyc/",
 		verbose_name=_('Photo ID(back)'),
 		# validators=[validate_kyc_file],
 		help_text=_("The back part of the user's valid photo id"))

	selfie_with_id = models.FileField(
 		storage="uploads/kyc/",
 		verbose_name=_('Selfie with ID'),
 		# validators=[validate_setting_image],
 		blank=True, null=True,
 		help_text=_("User's photo of themself with their id. The face of the user and the document must be visible")) 

	kyc_status = models.CharField(
		verbose_name=('KYC Status'),
		choices=ModelChoices.KYC_STATUS,
		default='Unverified',
		max_length=25,
		# blank=True, null=True,
		help_text=_("KYC status of the client.")
		)

	kyc_status_note = models.TextField(
 		verbose_name=_('KYC status note'),
 		editable=False,
 		blank=True, null=True,
 		help_text=_("Reason for current KYC status"))

	status_update_date = models.DateTimeField(
 		default=timezone.now,
 		verbose_name=_('Status update time'),
 		editable=False,
 		help_text=_('Timestamp when status was updated'))

	politically_exposed_person = models.CharField(
		verbose_name=_('Politically Exposed Person(PEP)'),
		choices=ModelChoices.PEP_CHOICES,
		max_length=16,
		default='not_pep',
		help_text=_("""A politically exposed person(PEP) is one who has been entrusted with 
			a prominent public function. A PEP generally present a higher risk for potential involvement in bribery
			and corruption by virtue of their position and the influence that they may hold. 'not_pep'
			implies the user is not politically exposed and 'pep' implies the user is. """))

	place_of_birth = models.CharField(
		verbose_name=_('Place of birth'),
		max_length=225,
		blank=True, null=True,
		help_text=_("User's place of birth"))

	identification_number = models.CharField(
		verbose_name=_('Identification number'),
		max_length=100,
		blank=True, null=True,
		help_text=_("User's identification number"))

	identification_issue_date = models.DateField(
		verbose_name=_('Identification issue date'),
		blank=True, null=True,
		help_text=_("The issue date of the user's identification document"))

	identification_expiry_date = models.DateField(
		verbose_name=_('Identification expiry date'),
		blank=True, null=True,
		help_text=_("The expiry date of the user's identification document"))

	kyc_submitted_ip_address = models.GenericIPAddressField(
		verbose_name=_('KYC submitted IP address'),
		blank=True, null=True,
		editable=False,
		help_text=_("User's IP address recorded at the time of registration")
		)

	registered_ip_address = models.GenericIPAddressField(
		verbose_name=_('Registered IP address'),
		blank=True, null=True,
		editable=False,
		help_text=_("User's IP address recorded at the time of registration. This address is compared to the kyc_submitted_ip_address to make sure the user is still within the same region")
		)

	# reference = models.CharField(
	# 	default=Generators.generate_reference,
	# 	verbose_name=_('Reference'),
	# 	max_length=10,
	# 	help_text=_('Auto generated refernce for KYC application. A transaction reference number helps to identify transactions in records and used to monitor transactions associuated with a card payment')
	# 	)

	us_citizen_tax_resident = models.BooleanField(
		default=False,
		verbose_name=_('US citizen tax resident'),
		help_text=_("Indicates whether the user is a citizen/tax resident of the US or not"))

	accept_terms = models.BooleanField(
		default=False,
		verbose_name=_('Accept terms'),
		help_text=_("Agreement collected from the user to accept the terms and conditions"))

	agreed_to_data_usage = models.BooleanField(
		default=False,
		verbose_name=_('Agreed to data usage'),
		help_text=_("Agreement collected from the user to gain consent to use their provided data"))


	citizenship = models.ForeignKey(
		Country,
		verbose_name=_('Citizenship'),
		on_delete=models.CASCADE,
		related_name='+',
		help_text=_("The citizenship of the user as shown in documents"))

	second_citizenship = models.ForeignKey(
		Country,
		blank=True, null=True,
		verbose_name=_('Second citizenship'),
		on_delete=models.CASCADE,
		related_name='+',
		help_text=_("Second citizenship of the user as shown in documents"))

	country_residence = models.ForeignKey(
		Country,
		verbose_name=_('Country of residence'),
		blank=True,
		on_delete=models.CASCADE,
		help_text=_("The country of residence of the user as shown in documents")
		)

	kyc_country = models.ForeignKey(
		Country,
		verbose_name=_('KYC Country'),
		blank=True, null=True,
		on_delete=models.PROTECT,
		related_name='kyc_country', #helps us resolve clashes with similar models
		help_text=_("The country which the KYC has been performed against the user. Each country has different KYC requirements")
		)

	user = models.ForeignKey(
		User,
		verbose_name=_('KYC User'),
		on_delete=models.CASCADE,
		help_text=_("The unique identifier of the user")
		)

	reviewer = models.ForeignKey(
		User,
		verbose_name=_('Reviewer'),
		blank=True, null=True,
		on_delete=models.CASCADE,
		related_name='kyc_reviewer',
		help_text=_("The KYC staff or representative who checked and reviewed the KYC application")
		)

	kyc_review_date = models.DateTimeField(
		verbose_name=_('KYC review date'),
		blank=True, null=True,
		editable=False,
		help_text=_("The country of residence of the user as shown in documents")
		)

	reviewer_ip_address = models.GenericIPAddressField(
		verbose_name=_('Reviewer IP address'),
		blank=True, null=True,
		editable=False,
		help_text=_("Reviewer's IP address recorded at the time of registration. This address is compared to the kyc_submitted_ip_address to make sure the user is still within the same region")
		)

	kyc_refused_code = models.CharField(
		verbose_name=_('KYC refused code'),
		max_length=35,
		choices=ModelChoices.KYC_REFUSE_REASON_CODE,
		blank=True, null=True,
		help_text=_("The reason for the refusal")
		)

	class Meta:
		verbose_name = _('KYC Application')
		verbose_name_plural = _('KYC Applications')
		db_table = 'kyc_applications'
		permissions = [
			("verify_kyc", _("Verify KYC Application")),
			("reject_kyc", _("Reject KYC Application")),
			("merge_kyc", _("Merge KYC Application with User Information")),
			]

	def __str__(self):
		return _("KYC #: ") + self.reference

	@property
	def age(self):
		return int((datetime.now().date() - self.date_of_birth).days / 365.25) #Calculates the user's age

	def get_user(self):
		return str(self.user.pk)

	get_object_user = property(get_user)

	# def clean_fields(self, exclude=None):
	# 	super().clean_fields(exclude=exclude)
	# 	if self.identification_issue_date == self.identification_expiry_date:
	# 		raise ValidationError(
	# 		{
	# 			'identification_issue_date': _("ID issue date and Expiry date cannot be the same."),
	# 		}

	# 			)
	# 	if self.identification_issue_date > datetime.today():
	# 		raise ValidationError(
	# 			{
	# 			'identification_issue_date': _("ID issue date is ahead of today."),
	# 		}
	# 			)
	# 	if self.identification_issue_date == datetime.today() or self.identification_expiry_date < date.today():
	# 		raise ValidationError(
	# 			{
	# 			'identification_issue_date': _("ID has expired."),
	# 		}
	# 			)
	

class KYCSetting(SingletonModel):
	#This model represents KYC settings and configs

	#Choices
	#Setting for if a user wants to use the manual or automatic KYC verification
	MANUAL = 'manual'  #Uses a KYC form that is filled and reviewed by a KYC staff
	AUTOMATIC = 'automatic'	#Uses an api service gotten from a KYC provider to complete the process

	KYC_SYSTEM_TYPE = (
		(MANUAL, _('Manual KYC')),
		(AUTOMATIC, _('Automatic KYC'))
		)

	singleton_instance_id = 1 

	enable_kyc = models.BooleanField(
		default=True,
		verbose_name=_('Enable KYC Verification'),
		help_text=_('Activates or Deactivates KYC application on the system'))

	allow_resubmission = models.BooleanField(
		default=False,
		verbose_name=_('Allow KYC Re-submission'),
		help_text=_("Allows User to resubmit KYC application if the previous attempt failed. This can only be done a number of times"))

	number_of_kyc_tries = models.PositiveIntegerField(
		default=1,
		verbose_name=_('Allow KYC tries'),
		help_text=_("Number of times a user is allowed to attempt KYC application"))

	run_check_on_expiry = models.BooleanField(
		default=False,
		verbose_name=_('Run check on Expiry'),
		help_text=_("Automated checks to find out if a user's ID has expired"))

	days_to_send_notification = models.PositiveIntegerField(
		default=30,
		verbose_name=_('Verification Notification'),
		help_text=_("If run check on expiry is turned on, indicate the number of days which the client receives a reminder of ID expiration and request for re-verification"))

	review_frequency = models.PositiveIntegerField(
		default=30,
		verbose_name=_('Review Frequency'),
		help_text=_("The amount of time on which a User must be reviewed"))

	kyc_system_type = models.CharField(
		choices=KYC_SYSTEM_TYPE,
		default=AUTOMATIC,
		verbose_name=_('KYC System Type'),
		max_length=10,
		help_text=_("Type of KYC system the User prefers to use"))


	class Meta:

		verbose_name = _('KYC Setting')
		verbose_name_plural = _('KYC Settings')

	def __str__(self):
		return 'KYC Setting'


