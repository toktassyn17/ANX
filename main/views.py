from django.shortcuts import render, redirect
from .models import Task
from .models import Subscriber
from .forms import TaskForm
from .forms import SubscriberForm
# def update(request):
#     task = Task.objects.all()
#     form = TaskForm(request.POST or None, instance = task)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     return render(request,'update',
#      {
#         'task': task,
#         'form': form,
#      } )

# def delete(request):
#     print(Tasks.objects)
#     return redirect('home')
# def delete(request,tasks_id):
#     tasks = Task.objects.get(pk = tasks_id )
#     tasks.delete()
#     return redirect('home')
def delete(request):
    tasks = Task.objects.first()
    tasks.delete()
    return redirect('home')

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page of website', 'tasks': tasks})


def about(request):

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



