from django.shortcuts import render
from frontend.models import TeamMember

# Create your views here.
def index(request):
	return render(request, 'pages/home.html')

def borrow(request):
	return render(request, 'pages/borrow.html')

def invest(request):
	return render(request, 'pages/invest.html')

def about_us(request):
	team_members = TeamMember.objects.all()
	context = {'team_members': team_members}
	return render(request, 'pages/about.html', context)

def teams(request):
	return render(request, 'pages/home.html')