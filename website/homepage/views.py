from django.shortcuts import render

# Dummy posts
posts = [
    {
        'author': 'Keanu Reano',
        'title': 'Blog Post 1',
        'content': 'Pariatur do ex nulla duis labore cillum dolore ad duis sunt cupidatat non ut ullamco. Laborum irure pariatur dolor culpa. Fugiat id fugiat non fugiat quis. Culpa nulla laboris sint deserunt laboris duis velit velit aute veniam eu ex. Cillum sit culpa tempor nisi commodo nulla dolor laboris sit proident ut nulla.',
        'date_posted': 'November 17, 2022'
    },
    {
        'author': 'Keanu Reano',
        'title': 'Blog Post 2',
        'content': 'Elit duis in esse eu occaecat elit commodo voluptate officia consequat minim dolore duis cupidatat. Incididunt elit consequat ipsum consectetur anim pariatur ut cillum aliqua deserunt. Do enim culpa velit cillum voluptate et.',
        'date_posted': 'November 19, 2022'
    }
]

# Create your views here.
def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'homepage/index.html', context)

def about(request):
    return render(request, 'homepage/about.html', {'title': 'About'})