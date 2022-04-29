from django.shortcuts import render, redirect
from .models import Task
from .models import Subscriber
from .forms import TaskForm
from .forms import SubscriberForm

def delete(request):
    tasks = Task.objects.first()
    tasks.delete()
    return redirect('home')

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page of website', 'tasks': tasks})


def about(request):
    # form = SubscriberForm(request.POST)
    # return render(request, 'main/about.html')
    # почему не работает спросить

    error = ''
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not right'

    form = SubscriberForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/about.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not right'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)



