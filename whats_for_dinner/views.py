from django.http import HttpResponse
from django.shortcuts import render
from whats_for_dinner.models import *
import random


def index(request):
    return render(request, 'whats_for_dinner/index.html')


def about(request):
    return render(request, 'whats_for_dinner/about.html')


def result(request):
    context_dict = {"food": random.choice(Food.objects.all())}
    context_dict["restaurant"] = context_dict["food"].restaurant
    return render(request, 'whats_for_dinner/result.html', context_dict)
