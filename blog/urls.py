from django.contrib import admin
from django.urls import path, include
from . import views # . represents current directory

urlpatterns = [
    # path('admin/', admin.site.urls), #this is if you want to show admin page
    #for showing home page
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]