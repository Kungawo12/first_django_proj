from django.shortcuts import render, redirect 
from .models import *

# Create your views here.

def home(request):
    data = {
        "movie" :Movie.objects.get(id=1)
    }
    
    return render(request, 'home.html',data)

def create_movie(request):
    Movie.objects.create(title = "Ant man",description = "Sci fi movies with advance technology", 
                        duration = 2)
    return redirect('/')