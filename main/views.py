from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, PersonalInfo, Story
import bcrypt

def index(request):
    return render(request, 'index.html')

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/profile')
        messages.error(request, 'INVALID CREDENTIALS')
        return redirect('/')
    messages.error(request, "Email doesn't exist, register an account")
    return redirect('/')

def register(request):
    errors = User.objects.validate_register(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect("/")
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt() ).decode()
    print(hashed_pw)

    new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_pw
    )
    request.session['user_id'] = new_user.id
    return redirect('/profile')

def profile(request):
    context = {
        'user' : User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'profile.html', context)

def logout(request):
    return redirect('/')

def stories(request):
    return render(request, 'stories.html')