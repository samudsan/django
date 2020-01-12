from django.shortcuts import render
from django.http import HttpResponse

post = [
    {'author': 'sandeep',
     'title': 'blog post1',
     'content': 'this is my Django project',
     'date_posted': 'Jan 12 2020'
     },

    {'author': 'dileep',
     'title': 'blog post1',
     'content': 'this is my selenium project',
     'date_posted': 'Dec 10 2019'
     }
]

def home(request):
    context = { # it will be used in render below
        'posts':post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'about'})


