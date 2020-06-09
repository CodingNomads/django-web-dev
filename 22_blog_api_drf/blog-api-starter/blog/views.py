from django.shortcuts import render
from .models import Post

# Create your views here.
def show_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'post_list.html', {'posts': posts})

def show_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})
