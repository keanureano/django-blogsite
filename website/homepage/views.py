from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'homepage/index.html', context)


def about(request):
    return render(request, 'homepage/about.html', {'title': 'About'})
