from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required
def feed(request):
    userids = []
    # gives you the whole user profile
    for user in request.user.profile.follows.all():
        # collecting the IDs of user's the user is following
        userids.append(user.id)
    # NOTE: (optional) uncomment the below line to also add own tweets:
    # userids.append(request.user.id)  # add own user ID
    # get all corresponding objects from the db and render 25 for display
    feed = Post.objects.filter(user_id__in=userids[:25])

    return render(request, 'feed.html', {'feed': feed})
