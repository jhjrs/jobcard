from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import JobCardForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Photo

def home(request):
    return render(request, 'cards/home.html')


@login_required
def job_card_view(request):
    if request.method == 'POST':
        form = JobCardForm(request.POST, request.FILES)
        if form.is_valid():
            job_card = form.save(commit=False)
            job_card.user = request.user
            job_card.save()
            return redirect('card')
    else:
        form = JobCardForm()
    return render(request, 'job_card.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('card')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'login.html')

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def display_users(request):
    users = User.objects.all()
    return render(request, 'cards/display_users.html', {'users': users})

def display_photos(request):
    photos = Photo.objects.all()
    return render(request, 'cards/display_photos.html', {'photos': photos})