from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """Strona główna dla aplikacji Learning Log"""

    return render(request, 'learning_logs/index.html')

def topics(request):
    """Wyświetlanie listy tematów"""

    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Wyświetla pojedyńczy temat i wszystkie powiązane z nim wpisy"""

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Dodaj nowy temat"""

    if request.method != 'POST':
        #Nie przekazano żadnych danych, należy utworzyć pusty formularz

        form = TopicForm()

    else:
        #Przekazano dane za pomocą żądania POST, należy je przetworzyć

        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}

    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Dodanie nowego wpisu do tematu"""

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #Nie przekazano żadnych danych należy utworzyć pusty formularz

        form = EntryForm()

    else:
        #Przekazano dane za pomocą żądania POST należy je przetworzyć

        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}

    return render(request, 'learning_logs/new_entry.html', context)
    
