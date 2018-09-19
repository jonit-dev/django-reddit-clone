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

    @staticmethod
    def filled_request_fields(request):
        # collect the field names that are empty
        empty_posts = []

        for data in request.POST:
            if not request.POST[data]:  # grab all data in request.POST that is empty
                empty_posts.append(data)

        # if request fields are empty all filled, return True. If not, return the ones that arent filled
        if len(empty_posts) > 0:

            pretty_posts = []
            for data in empty_posts:
                if "_" in data:
                    splitted_data = data.split("_")
                    data = " ".join(splitted_data[1:])
                    pretty_posts.append(data)

            if len(pretty_posts) > 0:
                return pretty_posts
            else:
                return empty_posts

        else:
            return True #if all request fields are valid
