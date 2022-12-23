from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'rating_status', 'currency']
    list_editable = ['year', 'rating', 'currency']
    ordering = ['rating']
    list_per_page = 6

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return "Зачем это смотреть?!"
        elif movie.rating < 70:
            return "Разок можно глянуть"
        elif movie.rating <= 85:
            return "Зачет"
        return 'Топчик'

admin.site.register(Movie, MovieAdmin)