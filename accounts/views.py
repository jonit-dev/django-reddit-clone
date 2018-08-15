from django.shortcuts import render

from classes.UIDisplay import *
from classes.user.Validate import *
from django.contrib.auth.models import User


def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register/index.html')

    if request.method == "POST":
        # VALIDATION =========================== #

        if Validate.check_user_exists(request.POST["user_email"]):
            return UIDisplay.alert(request, "accounts/register/index.html", "danger",
                                   "This user already exists. Try using a different e-mail or username")
        else:
            user = User.objects.create_user(request.POST["user_name"], request.POST["user_email"],
                                            request.POST["user_password"])

            if user:

                #login user



                return UIDisplay.alert(request, "accounts/register/index.html", "success",
                                       "Your account was created successfully")
            else:
                return UIDisplay.alert(request, "accounts/register/index.html", "danger",
                                       "Error while creating your user")

# else:
#     return UIDisplay.alert(request, "accounts/register/index.html", "danger",
#                            "This e-mail already exists in our database. Please, select another one")
