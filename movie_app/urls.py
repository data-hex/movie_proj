from . import views
from django.urls import path
from .views import ShowAllDirectors, ShowAllActors

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', ShowAllDirectors.as_view()),
    path('directors/<int:id_director>', views.show_one_director, name='director-detail'),
    path('actors', ShowAllActors.as_view()),
    path('actors/<int:id_actor>', views.show_one_actor, name='actor-detail')

]
