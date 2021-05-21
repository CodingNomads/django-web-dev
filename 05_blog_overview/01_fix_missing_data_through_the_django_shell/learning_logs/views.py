from django.shortcuts import render
from .models import Topic


# Create your views here.
def index(request):
    """The home page for learning logs."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Displays a list of all available topics."""
    topics = Topic.objects.order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
