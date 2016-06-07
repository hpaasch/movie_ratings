from django.contrib import admin

# Register your models here.
from movie_app.models import Rating, Rater, Movie

admin.site.register(Rating)
admin.site.register(Rater)
admin.site.register(Movie)
