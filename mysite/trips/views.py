from datetime import datetime

from django.shortcuts import render

from trips.models import Post


def hello_world(request):
    return render(request,
                  'hello_world.html',
                  {'current_time': datetime.now()})


def home(request):
    # get all the posts
    post_list = Post.objects.all()
    return render(request,
                  'home.html',
                  {'post_list': post_list})
