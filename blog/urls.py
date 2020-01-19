from django.contrib import admin
from django.urls import path, include
from . import views # . represents current directory
from .views import (
    PostListView,
    PostDetailedView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)


urlpatterns = [
    # path('admin/', admin.site.urls), #this is if you want to show admin page
    #for showing home page
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailedView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('about/', views.about, name='blog-about'),
]