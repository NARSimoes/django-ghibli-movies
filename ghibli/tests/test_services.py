
import os
from unittest.mock import patch
from django.test import TestCase

from ..services import get_movies, get_json_request


GHIBLI_BASE_URL = os.getenv("GHIBLI_API")
# mock values defined here, if we increase the tests
# this should be moved into static file (e.g. mock_movies.json)
mock_movies = [{
        "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
        "title": "Castle in the Sky",
        "description": "Movie Description Castle in the Sky",
        "director": "Hayao Miyazaki",
        "producer": "Isao Takahata",
        "release_date": "1986",
        "rt_score": "95",
        "people": ["TESTE"]
    },
    {
        "id": "12cfb892-aac0-4c5b-94af-521852e46d6a",
        "title": "Grave of the Fireflies",
        "description": "Movie description Grave of the Fireflies",
        "director": "Isao Takahata",
        "producer": "Toru Hara",
        "release_date": "1988",
        "rt_score": "97",
        "people": ["TESTE"]
    }
]

mock_persons = [{
        "id": "ba924631-068e-4436-b6de-f3283fa848f0",
        "name": "Ashitaka",
        "gender": "male",
        "age": "late teens",
        "eye_color": "brown",
        "hair_color": "brown",
        "films": [GHIBLI_BASE_URL +
                  "/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"],
        "species": GHIBLI_BASE_URL +
                "/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
        "url": GHIBLI_BASE_URL +
               "/people/ba924631-068e-4436-b6de-f3283fa848f0"
    },
    {
        "id": "030555b3-4c92-4fce-93fb-e70c3ae3df8b",
        "name": "Yakul",
        "age": "Unknown",
        "gender": "male",
        "eye_color": "Grey",
        "hair_color": "Brown",
        "films": [GHIBLI_BASE_URL + "/films/woowwwww"],
        "species": GHIBLI_BASE_URL +
                "/species/6bc92fdd-b0f4-4286-ad71-1f99fb4a0d1e",
        "url": GHIBLI_BASE_URL +
               "/people/030555b3-4c92-4fce-93fb-e70c3ae3df8b"
    }
]


class ServicesTests(TestCase):
    """
        Tests for get_json_request()
        - test_get_json_request_movies
        - test_get_json_request_empty_movies
        - test_get_json_request_people
        - test_get_json_request_empty_people
        Those tests could be improved for example testing
        with different status code (e.g. 500 internal
        server error).

        Tests for get_movies()
        - test_get_movies_with_empty_people
        - test_get_movies_with_empty_movies
        - test_get_movies_with_correct_values
        - test_get_movies_with_empty_values
    """
    @patch("ghibli.services.requests.get")
    def test_get_json_request_movies(self, mock_get):
        mock_get.return_value.json.return_value = mock_movies
        ghibli_movies = get_json_request(GHIBLI_BASE_URL + "/films")
        self.assertEqual(ghibli_movies, mock_movies)

    @patch("ghibli.services.requests.get")
    def test_get_json_request_empty_movies(self, mock_get):
        mock_get.return_value.json.return_value = []
        ghibli_movies = get_json_request(GHIBLI_BASE_URL + "/films")
        self.assertEqual(ghibli_movies, [])

    @patch("ghibli.services.requests.get")
    def test_get_json_request_people(self, mock_get):
        mock_get.return_value.json.return_value = mock_persons
        ghibli_people = get_json_request(GHIBLI_BASE_URL + "/people")
        self.assertEqual(ghibli_people, mock_persons)

    @patch("ghibli.services.requests.get")
    def test_get_json_request_empty_people(self, mock_get):
        mock_get.return_value.json.return_value = []
        ghibli_people = get_json_request(GHIBLI_BASE_URL + "/people")
        self.assertEqual(ghibli_people, [])

    def test_get_movies_with_empty_people(self):
        """Testing getting movies with empty people! Should return
        movies json but with an empty people array!"""
        movies_from_services = get_movies(mock_movies, [])
        expected_value = {"movies": [{
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
        self.assertEqual(movies_from_services, expected_value)

    def test_get_movies_with_empty_movies(self):
        """Testing getting movies with empty people! Should return
        movies json but with an empty people array!"""
        movies_from_services = get_movies([], mock_persons)
        self.assertEqual(movies_from_services, {})

    def test_get_movies_with_correct_values(self):
        """Testing getting movies with correct values! Getting two movies where
        just one movie match with one person from people."""
        movies_from_services = get_movies(mock_movies, mock_persons)
        expected_value = {"movies": [{
            "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
            "title": "Castle in the Sky",
            "description": "Movie Description Castle in the Sky",
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
         }]}
        self.assertEqual(movies_from_services, expected_value)

    def test_get_movies_with_empty_values(self):
        """Testing getting movies with empty values: movies and people!"""
        movies_from_services = get_movies([], [])
        self.assertEqual(movies_from_services, {})
