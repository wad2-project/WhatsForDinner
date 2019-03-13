from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, 'whats_for_dinner/index.html')


def about(request):
	return HttpResponse("About page")
