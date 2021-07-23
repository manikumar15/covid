from django.shortcuts import render

# Create your views here.

def animation_page(request):
	return render(request,'animation_page.html')

def home_page(request):
	return render(request,'home_page.html')

def search_page(request):
	return render(request,'search_page.html')

def dashboard(request):
	return render(request,'dashboard.html')