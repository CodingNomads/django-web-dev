from django.shortcuts import render
from .models import Topic, Entry


# Create your views here.
def index(request):
    """The home page for learning logs."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Displays a list of all available topics."""
    topics = Topic.objects.order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def entry(request, pk):
    """Displays the full text of a a learning entry."""
    entry = Entry.objects.get(pk=pk)
    return render(request, 'learning_logs/entry.html')
    