from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render()

def about(request):
    return HttpResponse('about page')

def contact(request):
    return HttpResponse('contact page')