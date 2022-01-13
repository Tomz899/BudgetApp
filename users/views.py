from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm

def register(request):
    if request.user.is_authenticated:
        return redirect('/budget')
    else:
        form = UserRegisterForm() # From forms.py - form inherit from django.contrib.auth.forms UserCreationForm, added email
        
        if request.method == "POST":       
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                new_user = form.cleaned_data.get('username')
                messages.success(request, new_user + f' Your account has been created! You are now able to login.')
                return redirect('login')
        return render(request, 'users/register.html', {'form': form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/budget')
    else:  
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')        
            user = authenticate(request, username=username, password=password)
                    
            if user is not None:
                login(request, user)
                return redirect('/budget')
            else:
                messages.info(request, 'Wrong username or password! Try again.')
        return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')