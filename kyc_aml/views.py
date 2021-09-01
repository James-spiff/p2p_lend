from django.shortcuts import render
from ipware import get_client_ip #get's the clients ip address
from .forms import KYCApplicationForm
from locations.models import Country
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction #a database transaction represents any change in a database
from p2p_lend.users.models import UserAddress


User = get_user_model()

def index(request):
	return render(request, "kyc_aml/index.html")


@login_required
def submit(request):
	if request.method == 'POST':
		form = KYCApplicationForm(request.POST, request.FILES) #posts the request to the database with the files attached to it
		if form.is_valid():
			country = get_object_or_404(Country, pk=int(request.POST.get('citizenship')))
			client_ip, is_routable = get_client_ip(request)
			kyc = form.save(commit=False) #save(commit=False) saves the data to the system memory but not the database
			kyc.identification_type = request.POST.get('identification_type')
			#kyc.photo_id = request.FILES['photo_id']
			kyc.proof_of_address_document = request.FILES['proof_of_address_document']
			kyc.user = request.user 
			kyc.legal_first_name = request.user.first_name
			kyc.legal_last_name = request.user.last_name
			kyc.email = request.user.email 
			kyc.country_residence = request.user.country_of_residence 
			kyc.citizenship = country
			kyc.kyc_submitted_ip_address = client_ip
			kyc.user.modified_date = timezone.now 
			#kyc.registered_ip_address = request.user.registered_ip_address 
			kyc.agreed_to_data_usage = True 
			kyc.accept_terms = True 
			kyc.us_citizen_tax_resident = True if country.iso2 == 'US' else False
			kyc.kyc_status ='pending'

			kyc.save()
			# if settings.SANDBOX:
			# 	kyc.kyc_status = 'Verified' if request.user.account_type == 'individual' else 'Action_Required'
			# else:
			# 	kyc.kyc_status = 'Pending' if request.user.account_type == 'individual' else 'Action_Required'
			# kyc.save()

			# Create user address record
			user_address = UserAddress(
				type = "current",
				address_line_1 = kyc.address_line_1,
				address_line_2 = kyc.address_line_2,
				state = kyc.state,
				city = kyc.city,
				country = kyc.country, 
				zip_post_code = kyc.zip_post_code,
				user = request.user 
				)

			user_address.save()

			# Update user records
			user_to_update = User.objects.select_for_update().filter(id=request.user.id)
			with transaction.atomic():	#atomic is a db transaction property which must be complete in it's entirety or have no effect at all(either all occurs or nothing). *From ACID properties
			#either all these updates occur or nothing
				for user in user_to_update:
					user.current_address = user_address
					user.permanent_address = user_address
					user.kyc_submitted = True
					user.kyc_complete = True 
					user.kyc.complete_date = timezone.now()
					user.kyc_status = 'pending'
					user.on_boarding_complete = True
					user.on_boarding_complete_date = timezone.now()
					user.save()

		print(form.errors)
		form = KYCApplicationForm(initial={
			'legal_first_name': request.user.first_name,
			'legal_last_name': request.user.last_name,
			'country_residence': request.user.country_of_residence,
			'citizenship': request.user.country_of_residence,
			'address_line_1': request.POST.get('address_line_1'),
			'address_line_2': request.POST.get('address_line_2'),
			'city': request.POST.get('city'),
			'state': request.POST.get('state'),
			'zip_post_code': request.POST.get('zip_post_code'),
			'identification_type': request.POST.get('identification_type'),
			'address_proof_type': request.POST.get('address_proof_type'),
			# 'photo_id': request.FILES['photo_id']
			})
		context = {'form': form}

		return render(request, 'kyc_aml/submit.html', context)
	else:
		form = KYCApplicationForm(initial={
			'legal_first_name': request.user.first_name,
			'legal_last_name': request.user.last_name,
			'country_residence': request.user.country_of_residence,
			'citizenship': request.user.country_of_residence,
			})
		context = {'form': form}

		return render(request, 'kyc_aml/submit.html', context)


def success(request):
	return render(request, "kyc_aml/success.html")
