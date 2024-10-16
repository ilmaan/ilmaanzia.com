from django.db import models
import re
from ckeditor.fields import RichTextField

class Information(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    mini_about = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    born_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    cv = models.FileField(blank=True, null=True)

    # Social Network
    github = models.CharField(max_length=200,blank=True, null=True)
    linkedin = models.CharField(max_length=200,blank=True, null=True)
    facebook = models.CharField(max_length=200,blank=True, null=True)
    twitter = models.CharField(max_length=200,blank=True, null=True)
    instagram = models.CharField(max_length=200,blank=True, null=True)
    googlescholar = models.CharField(max_length=200,blank=True, null=True, default="")

    def __str__(self):
        return self.name_complete


class Competence(models.Model):
        # Defining the possible types as choices
    COMPETENCE_TYPES = [
        ('programming_language', 'Programming Language'),
        ('framework', 'Framework'),
        ('front_end', 'Front-End'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('data_visualization', 'Data Visualization'),
    ]
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    image = models.FileField(upload_to='competence/', blank=True, null=True)
    icon = models.CharField(max_length=200, blank=True, default="fa-brands fa-2xl")

    # Adding type field with predefined choices
    type = models.CharField(
        max_length=50,
        choices=COMPETENCE_TYPES,  # Restricting input to predefined choices
        default='programming_language',  # Default type if none is chosen
        blank=False,
        null=False
    )

    def __str__(self):
        return self.title




class Education(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    the_year = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    the_year = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=False, null=False)
    image = models.ImageField(upload_to="projects/")
    tools = models.CharField(max_length=200, blank=False, null=False)
    demo = models.URLField()
    github = models.URLField()
    show_in_slider = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_project_absolute_url(self):
        return "/projects/{}".format(self.slug)

    def save(self, *args, **kwargs):
        self.slug = self.slug_generate()
        super(Project, self).save(*args, **kwargs)

    def slug_generate(self):
        slug = self.title.strip()
        slug = re.sub(" ", "_", slug)
        return slug.lower()



class Research(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=False, null=False)
    image = models.ImageField(upload_to="research/")
    tools = models.CharField(max_length=200, blank=True, null=False)
    demo = models.URLField()
    github = models.URLField()
    show_in_slider = models.BooleanField(default=False)
    file = models.FileField(null=True)

    def __str__(self):
        return self.title

    def get_project_absolute_url(self):
        return "/research/{}".format(self.slug)

    def save(self, *args, **kwargs):
        self.slug = self.slug_generate()
        super(Research, self).save(*args, **kwargs)

    def slug_generate(self):
        slug = self.title.strip()
        slug = re.sub(" ", "_", slug)
        return slug.lower()



class Message(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    send_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name
