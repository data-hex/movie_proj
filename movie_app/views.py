from django.shortcuts import render
from .models import Movie

# Create your views here.

def show_all_movie(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/all_movies.html', {'movies': movies})
