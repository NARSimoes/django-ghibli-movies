
"""
    Tasks holds all task to be execute by celery:
    - get_ghibli_movies
"""

from django.conf import settings
from django.core.cache import cache
from celery.utils.log import get_task_logger
from celery.signals import worker_ready

from ghiblimovies.celery import app
from .services import get_movies


logger = get_task_logger(__name__)


@worker_ready.connect  # launch task on start
@app.task(name="get_ghibli_movies")
def get_ghibli_movies(**kwargs):
    """Getting movies from api and setting it to cache."""
    logger.info("Starting Task: Get Ghibli movies from API!")

    movies = get_movies()
    if movies:
        cache.set(settings.KEY_CACHE_GHIBLI, movies, timeout=None)
