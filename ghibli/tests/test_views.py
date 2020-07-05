
from unittest.mock import patch
from django.test import TestCase, Client
from django.conf import settings
from django.urls import reverse

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
    """
        Testing ghibli movies list view()
        - test_status_code
        - test_template_used
        - test_ghibli_movies_list_view_with_empty_values
        - test_ghibli_movies_list_view
    """
    def setUp(self) -> None:
        self.client = Client()

    def test_status_code(self) -> None:
        """Testing the status code and template used!"""
        resp = self.client.get(reverse("ghibli_movies_view"))
        self.assertEqual(resp.status_code, 200)

    def test_template_used(self) -> None:
        """Testing the status code and template used!"""
        resp = self.client.get(reverse("ghibli_movies_view"))
        self.assertTemplateUsed(resp, 'ghibli/movies.html')

    @patch('django.core.cache.cache.get', return_value={"movies": []})
    def test_ghibli_movies_list_view_with_empty_values(self, test_func):
        """Testing """
        resp = self.client.get(reverse("ghibli_movies_view"))
        self.client.get(settings.KEY_CACHE_GHIBLI)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context["movies"], [])

    @patch('django.core.cache.cache.get', return_value=mocked_ghibli_movies)
    def test_ghibli_movies_list_view(self, test_func):
        """Testing getting mocked values from cache and check status
        and context from response!"""
        resp = self.client.get(reverse("ghibli_movies_view"))
        self.client.get(settings.KEY_CACHE_GHIBLI)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.context["movies"],
            mocked_ghibli_movies["movies"]
        )
