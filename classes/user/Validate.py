from django.contrib.auth.models import User


class Validate:

    @staticmethod
    def check_user_exists(email):

        if User.objects.filter(email=email).exists():
            return True
        else:
            return False

    @staticmethod
    def passwords_match(password1, password2):
        return password1 == password2
