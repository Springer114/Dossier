from django.db import models
import re

class UserManager(models.Manager):
    def validate_register(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email_pattern'] = "Invalid email address!"
        user_list = User.objects.filter(email = post_data['email'])
        if len(user_list) > 0:
            errors['email_duplicate'] = "Account already exists with email"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Password and Confirm Password must match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PersonalInfo(models.Model):
    aka = models.CharField(max_length = 90, blank = True)
    occupation = models.CharField(max_length = 255, blank = True)
    current_city = models.CharField(max_length = 255, blank = True)
    place_of_birth = models.CharField(max_length = 255, blank = True)
    date_of_birth = models.DateField(blank = True, null = True)
    gender = models.CharField(max_length = 45, blank = True)
    age = models.PositiveSmallIntegerField(blank = True, null = True)
    marital_status = models.CharField(max_length = 255, blank = True)
    person = models.ForeignKey(User, related_name = 'personal_information', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Story(models.Model):
    title = models.CharField(max_length = 45)
    body = models.TextField()
    creator = models.ForeignKey(User, related_name = 'stories', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)