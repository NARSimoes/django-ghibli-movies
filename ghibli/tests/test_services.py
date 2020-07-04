
import os

from django.test import TestCase
from django.test.client import RequestFactory

from ..services import get_movies


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
        "films": [os.getenv("GHIBLI_APU") +
                  "/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"],
        "species": os.getenv("GHIBLI_APU") +
                "/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
        "url": os.getenv("GHIBLI_APU") +
               "/people/ba924631-068e-4436-b6de-f3283fa848f0"
    },
    {
        "id": "030555b3-4c92-4fce-93fb-e70c3ae3df8b",
        "name": "Yakul",
        "age": "Unknown",
        "gender": "male",
        "eye_color": "Grey",
        "hair_color": "Brown",
        "films": [os.getenv("GHIBLI_APU") + "/films/woowwwww"],
        "species": os.getenv("GHIBLI_APU") +
                "/species/6bc92fdd-b0f4-4286-ad71-1f99fb4a0d1e",
        "url": os.getenv("GHIBLI_APU") +
               "/people/030555b3-4c92-4fce-93fb-e70c3ae3df8b"
    }
]


class ServicesTestCase(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_get_movies_with_correct_values(self):
        """Testing getting movies with correct values! Getting two movies where
        just one movie match with one person from people."""
        self.factory.get(
            os.getenv("GHIBLI_APU") + '/films',
            json=mock_movies
        )
        self.factory.get(
            os.getenv("GHIBLI_APU") + '/people',
            json=mock_persons
        )
        movies_from_services = get_movies()
        expected_value = [{
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
        self.assertEqual(movies_from_services, expected_value)

    def test_get_movies_with_empty_values(self):
        """Testing getting movies with empty values!"""
        self.factory.get('https://ghibliapi.herokuapp.com/films', json=[{}])
        self.factory.get('https://ghibliapi.herokuapp.com/people', json=[{}])
        movies_from_services = get_movies()
        self.assertEqual(movies_from_services, [])
