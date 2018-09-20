from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.http import JsonResponse
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

        if request_fields == True:  # If all request fields are valid

            # Create post resource

            # post = Post()
            # post.title = request.POST['post_title']
            # post.url = request.POST['post_url']
            # post.description = request.POST['post_description']
            # post.pub_date = timezone.datetime.now()
            # post.author = request.user
            # post.save() #save resource on database

            # Check if post url is in correct forma

            post_url = request.POST["post_url"]

            if not post_url.startswith("http://"):
                post_url = "http://" + post_url  # add to it

            post = Post(
                title=request.POST['post_title'],
                url=post_url,
                description=request.POST['post_description'],
                pub_date=timezone.datetime.now(),
                author=request.user
            )
            post.save()

            return UIDisplay.alert(request, "home.html", "success", "Your post was published!")
        else:

            return UIDisplay.alert(request, "posts/index.html", "danger",
                                   "One or more fields seems to be empty: " + ", ".join(request_fields))


@login_required
def upvote(request, post_id):
    if request.method == "POST":
        upvote_value = request.POST["value"]

        # get post by id
        post = get_object_or_404(Post, pk=post_id)
        post.votes_total += int(upvote_value, 2)  # convert to int
        post.save()

        return JsonResponse({
            'response': 'success',
            'votes': post.votes_total,
            'alert': {
                "type": "warning",

                "message": "We've received your upvote of " + request.POST["value"]
            }
        })


@login_required
def downvote(request, post_id):
    if request.method == "POST":
        downvote_value = request.POST["value"]

        # get post by id
        post = get_object_or_404(Post, pk=post_id)
        post.votes_total -= int(downvote_value, 2)  # convert to int
        post.save()

        return JsonResponse({
            'response': 'success',
            'votes': post.votes_total,
            'alert': {
                "type": "warning",
                "message": "We've received your downvote of " + request.POST["value"]
            }
        })


@login_required
def show(request):
    if (request.method == "GET"):
        # load post resource
        post = get_object_or_404(Post, pk=request.id)

        return render(request, "posts/show.html", {
            "post": post
        })
