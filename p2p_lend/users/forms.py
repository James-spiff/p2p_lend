# from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
#from allauth.account.forms import SignupForm
from django import forms
from locations.models import Country

User = get_user_model()

"""Check base.py django_allauth for other signup details e.g password field"""
#the password field can be added manually but cookiecutter already provides it for us in our base.py although it can be overwritten if needed



# class UserChangeForm(admin_forms.UserChangeForm):
#     class Meta(admin_forms.UserChangeForm.Meta):
#         model = User


# class UserCreationForm(forms.ModelForm):
#     error_messages = {
#         'password_mismatch': _("The two password fields didn't match."),
#     }
#     password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

#     password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput,
#                                 help_text=_("Enter the same password as above, for verification."))

#     # country = forms.ModelChoiceField(
#     #     queryset=Country.objects.filter(accept_signup=True),
#     #     empty_label=_('Country of Residence'))

#     class Meta:
#         model = User
#         fields = ('email',)

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         return password2

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

############################################################################

ACCOUNT_TYPE = (
    ('borrower', _('Borrower')),
    ('investor', _('Investor')),
)


class CustomSignupForm(forms.Form):
    account_type = forms.ChoiceField(
        choices=ACCOUNT_TYPE,
        help_text=_("Choose the type of account."))

    first_name = forms.CharField(max_length=50, label='First Names')

    last_name = forms.CharField(max_length=30, label='Last Names')

    email = forms.CharField(max_length=30, label='')

    country_of_residence = forms.ModelChoiceField(
        queryset=Country.objects.filter(accept_signup=True).order_by('name'),   #accept_signup=True only displays countries that are not banned as choices for signup. banned=True will do the opposite and display only banned countries
        empty_label=_('Country of Residence'),
        help_text=_('A proof of residence will be required.'))

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = _('Legal First & Middle Names')
        self.fields['last_name'].widget.attrs['placeholder'] = _('Legal Last Names')
        self.fields['email'].widget.attrs['placeholder'] = _('Enter a valid Email Address')
        # self.fields['country'].label = False
        self.fields['email'].help_text = _('So we can send you confirmation of your registration')
        self.fields['first_name'].help_text = _('As shown in your documents')
        self.fields['last_name'].help_text = _('As shown in your documents')
        # self.fields['account_type'].label = False
        # self.helper = FormHelper()
        # self.helper.form_show_labels = False

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        # user.country = self.cleaned_data['country']
        user.name = self.cleaned_data['first_name'] + " " + self.cleaned_data['last_name']
        # user.agreed_to_data_usage = True
        # user.accept_terms = True
        # user.privacy_policy = True
        # user.gdpr_opt_out = True
        # user.account_type = self.cleaned_data['account_type']
        user.save()


    def signup(self, request, user):
        # group = Group.objects.get(name=self.cleaned_data['account_type'].title()) #groups into borrower or lender
        # client_ip, is_routable = get_client_ip(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.country_of_residence = self.cleaned_data['country_of_residence']
        user.account_type = self.cleaned_data['account_type']
        user.name = self.cleaned_data['first_name'] + " " + self.cleaned_data['last_name']
        # user.registered_ip_address = client_ip
        # user.groups.add(group)
        # user.agreed_to_data_usage = True
        # user.accept_terms = True
        # user.privacy_policy = True
        # user.gdpr_opt_out = True
        # user.is_business = True if self.cleaned_data['account_type'] == 'company' else False
        # user.is_personal = True if self.cleaned_data['account_type'] == 'individual' else False
        # user.default_currency = get_object_or_404(Currency, code=self.cleaned_data['country'].currency) #sets the default currency to the users country of residence
        # user.time_zone = time_zone()
        user.save()

        return user
