from django.shortcuts import render,redirect
from .forms import *
from .models import *

def home(request):
    tasks = Task.objects.all()
    if request.method== 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TasksForm()
    context = {'tasks':tasks, 'form': form}
    return render(request, 'home.html', context)

def edit(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TasksForm(instance= tasks)
    if request.method == 'POST':
        form = TasksForm(request.POST, instance= tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'tasks':tasks, 'form': form}
    return render(request, 'edit.html', context)

def delete(request,pk):
    tasks = Task.objects.get(id=pk)
    form = TasksForm(instance= tasks)
    if request.method == 'POST':
        tasks.delete()
        return redirect('/')
    context = {'tasks':tasks, 'form': form}
    return render(request, 'delete.html', context)
