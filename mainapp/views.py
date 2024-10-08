from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from mainapp.form import UserRegistrationForm

# Create your views here.
@login_required
def dashboard(request):
    return render(request,'registration/dashboard.html',{'section':'dashboard'})

def home(request):
    return HttpResponse("Welcome to the homepage!")

def logout_view(request):
    logout(request)  # Logs out the user
    return render(request, 'logout.html') 

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log in the user after registration
            return redirect('dashboard')  # Redirect to dashboard after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

