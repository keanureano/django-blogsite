from django.shortcuts import render

# Dummy posts
posts = [
    {
        'author': 'Keanu Reano',
        'title': 'Blog Post 1',
        'content': 'Labore excepteur ullamco amet ut aliqua. Commodo aliqua tempor laborum sunt eiusmod.',
        'date_posted': 'November 17, 2022'
    },
    {
        'author': 'Keanu Reano',
        'title': 'Blog Post 2',
        'content': 'Nulla est dolore eu eiusmod laborum culpa deserunt laboris Lorem.',
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