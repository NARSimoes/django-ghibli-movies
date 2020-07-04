
from django.conf import settings
from django.shortcuts import render
from django.core.cache import cache


# @cache_page(60)
def ghibli_movies_list_view(request, *args, **kwargs):
    """View for ghibli movies list! Getting the list from cache,
    because we don't request (GET) data from API every page load!"""
    movies_list = cache.get(settings.KEY_CACHE_GHIBLI, [])
    return render(request, 'ghibli/movies.html', movies_list)
