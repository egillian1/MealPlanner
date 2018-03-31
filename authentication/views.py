from django.shortcuts import render
from django.http import HttpResponse
#from django.core.exceptions import ValidationError

from pprint import pprint
import logging
logger = logging.getLogger("docker.console")

def index(request):
    #return HttpResponse("You are at the login page")
    return render(request, 'authentication/login.html')

def login(request):
    return HttpResponse("Congration. You done it (log in).")

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
        #raise ValidationError("Passwords do not match")
        return render(request, 'authentication/register.html', {'error': 'Passwords do not match'})

    return HttpResponse("Registered successfully")
