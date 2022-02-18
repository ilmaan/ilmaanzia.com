from django.urls import path
from .import views
from .views import PostListView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('form/', views.form, name='form'),
]