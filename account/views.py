from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignuoForm
# Create your views here.



def signup(request):
    form = SignuoForm()
    if request.method =='POST':
        form = SignuoForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request, user)
            return redirect('/')
    return render(request, 'signup.html', {'form':form} )