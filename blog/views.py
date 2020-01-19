from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.http import HttpResponse #to send http code directly

#
# post = [
#     {'author': 'sandeep',
#      'title': 'blog post1',
#      'content': 'this is my Djangos. project',
#      'date_posted': 'Jan 12 2020'
#      },
#
#     {'author': 'dileep',
#      'title': 'blog post1',
#      'content': 'this is my selenium project',
#      'date_posted': 'Dec 10 2019'
#      }
# ]

def home(request):
    context = { # it will be used in render below
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #by default when we define classbased views it will
    #search template of type <app>/<model>_<type>.html
    context_object_name = 'posts'
    ordering = '-date_posted'
    paginate_by = 2

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author= user).order_by('-date_posted')


class PostDetailedView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView): # this will look for template post_form by default.
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


#for this user should be logged in and auth of the post should be same
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # this will look for template post_form by default.
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


#for this user should be logged in and auth of the post should be same
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})


