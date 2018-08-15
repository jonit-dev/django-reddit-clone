from django.shortcuts import render

from classes.UIDisplay import *


# SHOW FORM FOR RESOURCE CREATION
def index(request):
    return render(request, 'accounts/register/index.html')


# CREATE RESOURCE
def create(request):


    print(request.POST["user_email"])

    return UIDisplay.alert(request, "accounts/register/index.html", "success", "Your account was created successfully")
