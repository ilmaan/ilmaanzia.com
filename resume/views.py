from django.shortcuts import render
from .models import Resume, Post, Homelem , Key4 , Language, Framework, FrontBack , Database , Experience , Education , Pdf
from django.http import HttpResponse
from django.views.generic import ListView
from datetime import datetime

# Create your views here.

def home(request):
    homel = Homelem.objects.get()
    return render(request, 'resume/home.html',{"homel":homel})



def about(request):
    resume = Resume.objects.get()
    keys = Key4.objects.get()
    language = Language.objects.all()
    framework = Framework.objects.all()
    frontback = FrontBack.objects.all()
    database = Database.objects.all()
    experience = Experience.objects.all().reverse()
    education = Education.objects.all()
    pdf = Pdf.objects.get()
    homel = Homelem.objects.get()
    return render(request, 'resume/about.html',{'resume':resume,'keys':keys,'language':language,'framework':framework,'frontback':frontback,'database':database,'experience':experience,'education':education,'pdf':pdf,'homel':homel})

#def blog(request):
#      'posts' : Post.objects.all()
#  }
#  return render(request,'resume/blog.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'resume/blog.html'
    context_object_name = 'posts'

    ordering = ['-date']

#def blog(request):
#    post_objects = Post.objects.all()
#    item_name = request.GET.get('item_name')
#    if item_name != '' and item_name is not None:
#        post_objects = post_objects.filter(title__icontains=item_name)
#
#    return render(request, 'resume/blog.html', {'post_objects':post_objects})

def form(request):
    resume = Resume.objects.get()
    return render (request, 'resume/form.html' ,{"resume":resume})


def vcard(request):
    resume = Resume.objects.get()
    # keys = Key4.objects.get()
    # language = Language.objects.all()
    # framework = Framework.objects.all()
    # frontback = FrontBack.objects.all()
    # database = Database.objects.all()
    experience = Experience.objects.all().order_by('-id')
    education = Education.objects.all().order_by('-id')
    pdf = Pdf.objects.get()
    homel = Homelem.objects.get()
    # today = datetime.date.today()
    # print("TODAY--->",today)
    # year = int(today.year)
    # print("YEAR--->",year)

    current_datetime = datetime.now()

    # Extract the year
    current_year = int(current_datetime.year)

    print("AGEBEFORE--",resume.Age,"------>>",current_year)

    resume.Age = ((current_year - int(resume.Age)) )
    print("AGE--",resume.Age)
    return render (request, 'resume/vcard.html' ,{"resume":resume,"experience":experience,"education":education,"pdf":pdf,"homel":homel})