
from unittest.mock import patch
from django.test import TestCase
from django.core.cache import cache
from django.conf import settings
from ..tasks import get_ghibli_movies

mock_ghibli_movies = {"movies": [{
    "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
    "title": "Castle in the Sky",
    "description": "Movie Description Castle in the Sky",
    "director": "Hayao Miyazaki",
    "producer": "Isao Takahata",
    "release_date": "1986",
    "rt_score": "95",
    "people": []},
    {
    "id": "12cfb892-aac0-4c5b-94af-521852e46d6a",
    "title": "Grave of the Fireflies",
    "description": "Movie description Grave of the Fireflies",
    "director": "Isao Takahata",
    "producer": "Toru Hara",
    "release_date": "1988",
    "rt_score": "97",
    "people": []
}]}


class TasksTests(TestCase):
    """
        Testing get_ghibli_movies_task()
        - test_get_ghibli_movies_with_wrong_cache_key
        - test_get_ghibli_movies_empty_values
        - test_get_ghibli_movies
    """
    @patch('ghibli.tasks.get_movies', return_value=mock_ghibli_movies)
    def test_get_ghibli_movies_with_wrong_cache_key(self, test_func):
        """Testing the get_ghibli_movies task, getting data
        from wrong cache key."""
        get_ghibli_movies.apply()
        ghibli_cache = cache.get("wrong cache key")
        self.assertEqual(ghibli_cache, None)

    @patch('ghibli.tasks.get_movies', return_value={})
    def test_get_ghibli_movies_empty_values(self, test_func):
        """Testing the get_ghibli_movies task with empty values
        from get_movie(), here the service get_ghibli_movies
        is mocked because the goal is to test just the task!"""
        get_ghibli_movies.apply()
        ghibli_cache = cache.get(settings.KEY_CACHE_GHIBLI)
        self.assertEqual(ghibli_cache, mock_ghibli_movies)

    @patch('ghibli.tasks.get_movies', return_value=mock_ghibli_movies)
    def test_get_ghibli_movies(self, test_func):
        """Testing the get_ghibli_movies task, here the service
        get_ghibli_movies is mocked because the goal is to test
        just the task!"""
        get_ghibli_movies.apply()
        ghibli_cache = cache.get(settings.KEY_CACHE_GHIBLI)
        self.assertEqual(ghibli_cache, mock_ghibli_movies)
