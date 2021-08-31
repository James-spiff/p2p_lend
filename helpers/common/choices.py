from django.utils.translation import gettext_lazy as _

class ModelChoices():

	#proof of address type(documents used for proof of address)
	BANK_STATEMENT = "BANK_STATEMENT"
	CREDIT_CARD_STATEMENT = "CREDIT_CARD_STATEMENT"
	UTILITY_BILL = "UTILITY_BILL"

	PROOF_OF_ADDRESS_TYPE = (
		(BANK_STATEMENT, _("Bank Statement")),
		(CREDIT_CARD_STATEMENT, _("Credit Card Statement")),
		(UTILITY_BILL, _("Utility Bill"))
		)

	#identification type
	PHOTO_IDENTIFICATION_TYPE = (
		('national_id', _("National ID")),
		('passport', _("International Passport")),
		('drivers_license', _("Drivers License"))
		)

	KYC_STATUS = (
        ('unverified', _('Unverified')),
        ('pending', _('Pending')),
        ('verified', _('Verified')),
        ('action_required', _('Action Required')),
        ('cancelled', _('Cancelled')),
        ('rejected', _('Rejected'))
        )

	PEP_CHOICES = (
		('not_pep', _("No, I am not politically exposed")),
		('pep', _("Yes, I am politically exposed"))
		)

	#codes used to flag kyc
	KYC_REFUSE_REASON_CODE = (
		('EXPIRED_DOCUMENT', _("Document expired")),
		('DOCUMENT_DOES_NOT_MATCH_USER_DATA', _("Document doesn't match user data")),
		)
