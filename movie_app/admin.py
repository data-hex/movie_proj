from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget']
    list_editable = ['year']
    ordering = ['rating']
    list_per_page = 5

admin.site.register(Movie, MovieAdmin)