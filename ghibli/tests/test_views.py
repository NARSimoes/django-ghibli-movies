
from unittest.mock import patch
from django.test import TestCase
from django.conf import settings


mocked_ghibli_movies = {"movies": [{
    "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
    "title": "Castle in the Sky",
    "description": "Movie description Castle in the Sky",
    "director": "Hayao Miyazaki",
    "producer": "Isao Takahata",
    "release_date": "1986",
    "rt_score": "95",
    "people": ["Ashitaka"]},
    {
        "id": "12cfb892-aac0-4c5b-94af-521852e46d6a",
        "title": "Grave of the Fireflies",
        "description": "Movie description Grave of the Fireflies",
        "director": "Isao Takahata",
        "producer": "Toru Hara",
        "release_date": "1988",
        "rt_score": "97",
        "people": []
    }]
}


class GhibliViewsTest(TestCase):

    @patch('django.core.cache.cache.get', return_value=mocked_ghibli_movies)
    def test_ghibli_movies_list_view(self, cache):
        cache_get = self.client.get(settings.KEY_CACHE_GHIBLI)
        self.assertTemplateUsed(cache_get, 'ghibli/movies.html')
