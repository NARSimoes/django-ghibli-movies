
from unittest.mock import patch
from django.test import TestCase
from django.core.cache import cache
from django.conf import settings
from ..tasks import get_ghibli_movies

mock_ghibli_movies = {"movies": [{"id": "test"}, {"id": "test_movies"}]}


class TestTasks(TestCase):

    @patch('ghibli.tasks.get_ghibli_movies', return_value=mock_ghibli_movies)
    def test_get_ghibli_movies(self, test):
        """Testing the get_ghibli_movies task, here the service get_ghibli_movies
        is mocked because the goal is to test just the task!"""
        ghibli_task = get_ghibli_movies.s().apply()
        ghibli_cache = cache.get(settings.KEY_CACHE_GHIBLI)
        self.assertEqual(ghibli_cache, mock_ghibli_movies)
