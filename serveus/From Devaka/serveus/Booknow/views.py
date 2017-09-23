from django.shortcuts import render
from django.http import HttpResponse

def booknow(request):
	return render(request, 'Booknow/booknow.html')