from django.shortcuts import render

from classes.UIDisplay import *
from classes.user.Validate import *
from django.contrib.auth.models import User  # User Model

from django.contrib.auth import authenticate, login, logout  # login


def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register/index.html')

    if request.method == "POST":
        # VALIDATION =========================== #

        if Validate.check_user_exists(request.POST["user_email"]):
            return UIDisplay.alert(request, "accounts/register/index.html", "danger",
                                   "This user already exists. Try using a different e-mail or username")

        # add check password match

        else:
            new_user = User.objects.create_user(request.POST["user_name"], request.POST["user_email"],
                                                request.POST["user_password"])

            if new_user:

                # # login user
                # user = authenticate(email=request.POST["user_email"], password=request.POST["user_password"])
                #
                # if user is not None:
                return UIDisplay.alert(request, "accounts/register/index.html", "success",
                                       "Your account was created successfully")
            # else:
            #     return UIDisplay.alert(request, "accounts/register/index.html", "danger",
            #                            "Error while trying to login your user")
            #

            else:
                return UIDisplay.alert(request, "accounts/register/index.html", "danger",
                                       "Error while creating your user")


def signin(request):
    if request.method == "GET":
        return render(request, 'accounts/login/index.html')

    if request.method == "POST":

        # lets try to login this user
        user = authenticate(username=request.POST["user_email"], password=request.POST["user_password"])

        if user is not None:
            print("Authenticating user... {}".format(user))

            login(request, user)
            return UIDisplay.alert(request, "home.html", "success", "You're now logged in")
        else:
            return UIDisplay.alert(request, "home.html", "danger", "Invalid credentials. Try again.")

def signout(request):

    logout(request)

    return UIDisplay.alert(request, "home.html", "primary", "You're now logged out")
