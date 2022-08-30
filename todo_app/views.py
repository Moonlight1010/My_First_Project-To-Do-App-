from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.
def taskview(request):
    if 'q' in request.GET:
        q = request.GET['q']
        tasks = Task.objects.filter(title__icontains=q)
    else:
        tasks = Task.objects.all()
    context = {
        'tasks':tasks,
    }
    return render(request, 'todo_app/taskview.html', context)

def taskform(request):
    form = TaskForm(request.POST)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('taskview-page')
        else:
            form = TaskForm()
    else:
        form = TaskForm()
    context = {
        'form':form
    }
    return render(request, 'todo_app/taskform.html', context)
def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST,instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('taskview-page')
        else:
            form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task)
    context = {
        'task':task,
        'form':form
    }
    return render(request, 'todo_app/taskupdate.html', context)
def delete_view(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('taskview-page')
    
