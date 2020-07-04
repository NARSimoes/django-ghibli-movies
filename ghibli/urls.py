
from django.urls import path
from .views import ghibli_movies_list_view


urlpatterns = [
    path('movies/', ghibli_movies_list_view, name='ghibli_movies_view'),
]
