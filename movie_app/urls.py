from . import views
from django.urls import path
from .views import ShowAllDirectors, ShowAllActors, ShowOneDirector, ShowOneActor

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', ShowAllDirectors.as_view()),
    path('directors/<int:pk>', ShowOneDirector.as_view(), name='director-detail'),
    path('actors', ShowAllActors.as_view()),
    path('actors/<int:pk>', ShowOneActor.as_view(), name='actor-detail')

]
