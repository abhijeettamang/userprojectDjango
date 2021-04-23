from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def base(request):
    return render(request, '/base')
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')

def homeUser(request):
    context = {}
    if request.method == 'POST':
        a = request.POST.get('first')
        b = request.POST.get('second')
        if a and b:
            context['result'] = int(a) + int(b)
    return render(request, 'home.html', context)
  
def add(request):
    context = {}
    if request.method == 'POST':
        a = request.POST.get('first')
        b = request.POST.get('second')
        if a and b:
            context['result'] = int(a) + int(b)
    return render(request, 'add.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username = username, password = password)
        #check if user has entered correct credentials
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/home')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')