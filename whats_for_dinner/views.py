from django.http import HttpResponse


def index(request):
	return HttpResponse("What's for Dinner?")
