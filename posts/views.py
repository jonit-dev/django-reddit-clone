from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.utils import timezone

from classes.UIDisplay import *
from classes.validate.Validate import *
from posts.models import Post


@login_required
def create(request):
    if request.method == "GET":

        # show form to create a post

        return render(request, "posts/index.html")

    elif request.method == "POST":

        # Create a new post

        # Validate if all fields are present

        request_fields = Validate.filled_request_fields(request)

        if request_fields == True: #If all request fields are valid

            # Create post resource

            # post = Post()
            # post.title = request.POST['post_title']
            # post.url = request.POST['post_url']
            # post.description = request.POST['post_description']
            # post.pub_date = timezone.datetime.now()
            # post.author = request.user
            # post.save() #save resource on database

            post = Post(
                title=request.POST['post_title'],
                url=request.POST['post_url'],
                description=request.POST['post_description'],
                pub_date=timezone.datetime.now(),
                author=request.user
            )
            post.save()

            return UIDisplay.alert(request, "posts/index.html", "success", "Your post was published!")
        else:

            return UIDisplay.alert(request, "posts/index.html", "danger",
                                   "One or more fields seems to be empty: " + ", ".join(request_fields))
