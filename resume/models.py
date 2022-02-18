from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Resume(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Nationality = models.CharField(max_length=30)
    Freelance = models.CharField(max_length=30, default='Available')
    Address = models.CharField(max_length=30)
    Phone = models.CharField(max_length=14)
    Email = models.CharField(max_length=30)
    Linkedin = models.CharField(max_length=50)
    Github = models.CharField(max_length=30)
    Languages = models.CharField(max_length=30)
    def __str__(self):
        return self.FirstName


class Pdf(models.Model):
    file = models.FileField(null=True)



class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    pdf = models.FileField(null=True)

    def __str__(self):
        return self.title


class Form(models.Model):
    yname = models.CharField(max_length=30)
    yemail = models.CharField(max_length=30)
    ysubject = models.CharField(max_length=30)
    ymessage = models.TextField()
    def __str__(self):
        return self.yemail

class Homelem(models.Model):
    profile = models.ImageField(upload_to='images/')
    Name = models.CharField(max_length=30)
    About = models.TextField()


class Key4(models.Model):
    No1 = models.CharField(max_length=10)
    Dsc1 = models.CharField(max_length=40)

    No2 = models.CharField(max_length=10)
    Dsc2 = models.CharField(max_length=40)

    No3 = models.CharField(max_length=10)
    Dsc3 = models.CharField(max_length=40)

    No4 = models.CharField(max_length=10)
    Dsc4 = models.CharField(max_length=40)



class Language(models.Model):
    skilset = models.CharField(max_length=10)
    value = models.IntegerField(max_length=10)
    def __str__(self):
        return self.skilset

class Framework(models.Model):
    skilset = models.CharField(max_length=10)
    value = models.IntegerField(max_length=10)
    def __str__(self):
        return self.skilset

class FrontBack(models.Model):
    skilset = models.CharField(max_length=10)
    value = models.IntegerField(max_length=10)
    def __str__(self):
        return self.skilset

class Database(models.Model):
    skilset = models.CharField(max_length=10)
    value = models.IntegerField(max_length=10)
    def __str__(self):
        return self.skilset

class Experience(models.Model):
    Time = models.CharField(max_length=20)
    Title = models.CharField(max_length=40)
    Dsc = models.CharField(max_length=40)
    def __str__(self):
        return self.Title

class Education(models.Model):
    Time = models.CharField(max_length=20)
    Title = models.CharField(max_length=40)
    Dsc = models.CharField(max_length=40)
    def __str__(self):
        return self.Title

