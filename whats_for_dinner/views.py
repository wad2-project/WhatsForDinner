from django.http import *
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from whats_for_dinner.models import *
from whats_for_dinner.forms import *
import random


def index(request):
    return render(request, 'whats_for_dinner/index.html')


def about(request):
    return render(request, 'whats_for_dinner/about.html')


def result(request):
    context_dict = {"food": random.choice(Food.objects.all())}
    context_dict["restaurant"] = context_dict["food"].restaurant
    return render(request, 'whats_for_dinner/result.html', context_dict)


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "picture" in request.FILES:
                profile.picture = request.FILES["picture"]

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, "whats_for_dinner/register.html",
                  {"user_form": user_form, "profile_form": profile_form, "registered": registered})


def user_login(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))

            else:
                return HttpResponse("Your whats_for_dinner account is disabled.")

        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, "whats_for_dinner/login.html", {})


@login_required
def favourites(request):
    return render(request, "whats_for_dinner/favourites.html", {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
