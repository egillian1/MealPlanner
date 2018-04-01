from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#from django.core.exceptions import ValidationError

from pprint import pprint
import logging
logger = logging.getLogger("docker.console")

def index(request):
    #return HttpResponse("You are at the login page")
    return render(request, 'authentication/login.html')

def logIntoSite(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #return reverse('mealplanner:index')
    else:
        return HttpResponse("Login failed.")

def register(request, error = ""):
    if(request.method == "GET"):
        return render(request, 'authentication/register.html')
    post = request.POST
    username = post['username']
    password = post['password']
    confirm = post['confirm']
    logger.info("User: " + username + " Pass: " + password)

    if(password != confirm):
        logger.info('passwords do not match')
        return render(request, 'authentication/register.html', {'error': 'Passwords do not match'})

    if(len(password) < 7):
        logger.info('password too short')
        return render(request, 'authentication/register.html', {'error': 'Password is too short'})

    newUser = User.objects.create_user(username, username, password)
    newUser.save()
    return HttpResponse("Registered successfully")
