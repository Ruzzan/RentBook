from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def Signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username already taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.first_name = request.POST['firstname']
                user.last_name = request.POST['lastname']
                user.save()
                auth.login(request, user)
                messages.success(request, 'You have been registered. You can login now.')
                return redirect('login')
        else:
            return render(request, 'accounts/signup.html', {'error':'Password is incorrect'})
    else:
        return render(request, 'accounts/signup.html')

def Login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                messages.success(request, 'Welcome to BookenT ' + user.username)
                return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Invalid username or password.'})
    
    return render(request, 'accounts/login.html')

def Logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

