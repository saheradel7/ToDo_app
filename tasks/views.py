from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

@login_required
def index(request):
    form = TaskForm()
    tasks =Task.objects.filter(user = request.user)
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect('/')
    return render(request , 'list.html', {'tasks':tasks ,'form':form})



    # tasks = Task.objects.all()
    # form = TaskForm()
    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/')

    # context = {'tasks': tasks, 'form':form}
    # return render(request, 'list.html', context )


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect("/")
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)