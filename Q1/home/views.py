from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

from home.models import TaskManager

def home(request):
    return render(request, 'index.html')

def tasks(request):
    try:
        data = TaskManager.objects.all()
        context = {'tasks': data}
    except Exception as e:
        context = {'tasks': 'Data Not Found'}
    return render (request, 'tasks.html', context)

@login_required(login_url='login')
@permission_required('home.add_profile', login_url='tasks')
def taskAdd(request):
    form = TaskManager()
    if request.method == 'POST':
        myData = TaskManager(request.POST)
        if myData.is_valid():   
            myData.save()
            messages.success(request, 'Task Added Successfully')
            return redirect('tasks')
    context = {'form': form}
    return render (request, 'taskAdd.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Credentials!')
        # print(username, password)
    return render (request, 'login.html')
    
def logoutPage(request):
    logout(request)
    return redirect('home')