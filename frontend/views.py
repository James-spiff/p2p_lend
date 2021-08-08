from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'pages/home.html')

def borrow(request):
	return render(request, 'pages/borrow.html')

def invest(request):
	return render(request, 'pages/invest.html')

def about_us(request):
	return render(request, 'pages/about.html')

def teams(request):
	return render(request, 'pages/home.html')