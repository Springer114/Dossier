from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Story
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
        date_of_birth = request.POST['date_of_birth'],
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
    request.session.clear()
    return redirect('/')

def edit_profile(request, user_id):
    context = {
        'user' : User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'edit_profile.html', context)

def update_profile(request, user_id):
    user = User.objects.get(id = user_id)

    errs = User.objects.validate_user_update(request.POST)
    if errs:
        for value in errs.values():
            messages.error(request, value)
        return redirect(f'/profile/edit/{user.id}')

    user.aka = request.POST['aka']
    user.occupation = request.POST['occupation']
    user.current_city = request.POST['current_city']
    user.place_of_birth = request.POST['place_of_birth']
    user.gender = request.POST['gender']
    user.age = request.POST['age']
    user.marital_status = request.POST['marital_status']
    user.education = request.POST['education']
    user.about = request.POST['about']
    user.save()
    return redirect('/profile')

def stories(request):
    context = {
        'user' : User.objects.get(id = request.session['user_id']),
        'all_stories' : Story.objects.all()
    }
    return render(request, 'stories.html', context)

def create_story(request):
    new_story = Story.objects.create(
        title = request.POST['title'],
        body = request.POST['body'],
        creator = User.objects.get(id = request.session['user_id'])
    )

    request.session['story_id'] = new_story.id

    return redirect('/stories')

def edit_story(request, story_id):
    story = Story.objects.get(id = story_id)
    story.title = request.POST['title']
    story.body = request.POST['body']
    story.save()
    return redirect('/stories')

def delete_story(request, story_id):
    story = Story.objects.get(id = story_id)
    story.delete()
    return redirect('/stories')