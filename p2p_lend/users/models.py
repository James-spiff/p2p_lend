from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
from locations.models import Country, State, City

class UserAddress(models.Model):

    #Gives our address a unique id
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text=_("""The unique identifier of the instance this object belongs to.
                    Mandatory, unless a new instance to create is given."""))

    user = models.ForeignKey(
        'User',
        on_delete=models.PROTECT,
        verbose_name=_('User'),
        help_text=_('The user that owns the adress'))

    address_line_1 = models.CharField(
        max_length=125,
        verbose_name=_('Adress line 1'),
        help_text=_('Adress line 1 of the user'))

    address_line_2 = models.CharField(
        max_length=125,
        verbose_name=_('Adress line 2'),
        blank=True, null=True,
        help_text=_('Adress line 2 of the user'))

    state = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        verbose_name=_('State'),
        help_text=_('State of residence'))

    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        verbose_name=_('City'),
        help_text=_('City of residence'))

    zip_post_code = models.CharField(
        max_length=20,
        verbose_name=_('Zip code'),
        help_text=_('User zip code'))

    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        verbose_name=_('Country'),
        help_text=_('Country of residence'))

    class Meta:
        verbose_name=_('User Adress')
        verbose_name_plural=_('User Adresses')

    def __str__(self):
        return self.name



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Default user for P2P Lending."""

    #User choices. below is an enum
    KYC_STATUS = (
        ('unverified', _('Unverified')),
        ('pending', _('Pending')),
        ('verified', _('Verified')),
        ('action_required', _('Action Required')),
        ('cancelled', _('Cancelled')),
        ('rejected', _('Rejected')),
        )

    #: First and last name do not cover name patterns around the globe
    objects = UserManager()  #remember to register the UserManager to avoid errors

    name = CharField(_("Name of User"), blank=True, max_length=255)
    username = None #we use our email address to login instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text=_("""The unique identifier of the instance this object belongs to.
                    Mandatory, unless a new instance to create is given."""))

    first_name = models.CharField(
        verbose_name=_('First names'),
        max_length=125,
        blank=True, null=True,
        help_text=_("Legal First names of the client."))

    last_name = models.CharField(
        verbose_name=_('Last names'),
        max_length=125,
        blank=True, null=True,
        help_text=_("Legal Last names of the client."))

    email = models.EmailField(
        verbose_name=_('Email Address'),
        max_length=150,
        unique=True,
        help_text=_("Email address of the client."))

    current_adress = models.ForeignKey(
        UserAddress,
        on_delete=models.PROTECT,
        verbose_name=_('Current Adress'),
        blank=True, null=True,
        related_name='+', #this stops it from clashing with permanent address
        help_text=_("Current adress of the client."))

    permanent_adress = models.ForeignKey(
        UserAddress,
        on_delete=models.PROTECT,
        verbose_name=_('Permanent Adress'),
        blank=True, null=True,
        related_name='+',
        help_text=_("Permanent adress of the client."))

    contact_number = models.CharField(
        verbose_name=_('Contact Number'),
        max_length=50,
        blank=True, null=True,
        help_text=_("Contact number of the client."))

    date_of_birth = models.DateField(
        verbose_name=_('Date of Birth'),
        blank=True, null=True,
        help_text=_("Client's date of birth."))

    kyc_complete = models.BooleanField(
        verbose_name=_('KYC Complete'),
        default=False,
        help_text=_("Flag to determine if customer has completed KYC verification."))

    kyc_complete_date = models.DateTimeField(
        verbose_name=_('KYC Completion Date'),
        blank=True, null=True,
        help_text=_("Timestamp for KYC verification."))

    kyc_status = models.CharField(
        verbose_name=('KYC Status'),
        choices=KYC_STATUS,
        default='Unverified',
        max_length=15,
        blank=True, null=True,
        help_text=("KYC status of the client.")
        )

    onboarding_complete = models.BooleanField(
        verbose_name=_('Completed Onboarding'),
        default=False,
        help_text=_("Flag to determine if customer has completed onboarding."))

    onboarding_complete_date = models.DateTimeField(
        verbose_name=_('Onboarding Completion Date'),
        blank=True, null=True,
        help_text=_("Timestamp for onboarding completion."))

    kyc_submitted = models.BooleanField(
        verbose_name=_('KYC Submitted'),
        default=False,
        help_text=_("Flag to determine if customer has submitted their KYC."))

    social_security_number = models.CharField(
        verbose_name=_('Social Security Number'),
        max_length=50,
        blank=True, null=True,
        help_text=_("Social security number of the client."))

    place_of_birth = models.CharField(
        verbose_name=_('Place of Birth'),
        max_length=150,
        blank=True, null=True,
        help_text=_("Client's place of birth."))

    verification_date = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Verification Date'),
        blank=True, null=True,
        editable=False,
        help_text=_("Timestamp when client's profile was verified."))

    registered_ip_address = models.GenericIPAddressField(
        verbose_name=_('Registered IP Address'),
        blank=True, null=True,
        editable=False,
        help_text=_("Client's ip address recorded at the time of registration."))

    country_of_residence = models.ForeignKey(
        Country,
        verbose_name=_('Country of Residence'),
        blank=True, null=True,
        on_delete=models.SET_NULL,
        help_text=_("Client's country of residence. KYC verification will be applied to this country with proof of residence."))

    job_title = models.CharField(
        verbose_name=_('Job Title'),
        max_length=125,
        blank=True, null=True,
        help_text=_("Client's job title."))

    default_currency = models.CharField(
        verbose_name=_('Default Currency'),
        max_length=3,
        default= 'EUR',
        blank=True, null=True,
        help_text=_("Default currency of the borrower."))

    #appending_cash_balance
    #time_zone
    #salutation
    #higher_qualification
    #passout_year
    #investment_limit
    #fund_committed
    #escrow_account_number
    #tax_id


    class Meta:
        verbose_name = _('Register User')
        verbose_name_plural = _('Registered Users')


    def __str__(self):
        return self.email


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.id})
