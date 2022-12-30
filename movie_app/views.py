from django.shortcuts import render, get_object_or_404
from .models import Movie, Director
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


# Create your views here.

def show_all_movie(request):
    # movies = Movie.objects.order_by('-rating')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('hello'),
        new_budget=F('budget') + 100,
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('name'))
    return render(request, 'movie_app/all_movies.html',
                  {'movies': movies,
                   'agg': agg
                   })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {'movie': movie})


def show_all_directors(request):
    directors = Director.objects.all
    return render(request, 'movie_app/all_directors.html', {'directors': directors})


def show_one_director(request, id_director: int):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'movie_app/one_director.html', {'director': director})
