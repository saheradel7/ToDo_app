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


@login_required
def updateTask(request, pk):
    task = Task.objects.get(id=pk , user =request.user)
    
    if request.method =='POST':
        form = TaskForm(request.POST,instance= task)
        if form.is_valid():
            t = form.save(commit = False)
            t.user = request.user
            t.save()
        return redirect('/')
    else:
        form = TaskForm(instance= task)

    return render(request, 'update_task.html' , {'tasks':task ,'form':form})



@login_required
def deleteTask(request, pk):
    Task.objects.get(id=pk,user =request.user).delete()
    return redirect('/')


@login_required
def check(request, pk):
    task= Task.objects.get(id=pk,user =request.user)
    if task.completed == True :
        task.completed = False
    elif task.completed == False:
        task.completed = True
    task.save()
    return redirect('/')


