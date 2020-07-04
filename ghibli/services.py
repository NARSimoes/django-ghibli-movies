
"""
    All services to communicate with external API:
    - get_movies()
"""

import logging
import requests


logger = logging.getLogger(__name__)


def get_movies():
    """
    Request movies and people from the ghibli api. Getting people
    from the people endpoint and joining that persons into movies
    if there are relationships between both.
    :return: {"movies": movies_list}
    """
    logger.info("Get Movies from API in services!")

    # getting movies
    movies = get_json_request('https://ghibliapi.herokuapp.com/films')
    if not movies:
        return {}

    people = get_json_request("https://ghibliapi.herokuapp.com/people")

    # clear people in list to ensure we clean all broken people data
    [i["people"].clear() for i in movies]

    for person in people:
        person_movies = person["films"]
        for pmovie in person_movies:
            id_movie = pmovie.split("/")[-1]
            # checking if we have movies for this person, if we have
            # append the name into people
            check_this_movie_id(id_movie, person, movies)

    movies_list = {'movies': movies}
    logger.info("Movies list in services:", movies_list)
    return movies_list


def check_this_movie_id(id_movie, person, movies):
    """
    Checking if we have this movie id in our movies. If yes,
    let's append the person name into people!
    :param id_movie:
    :param person:
    :param movies:
    :return:
    """
    for movie in movies:
        # found movie?
        if id_movie in movie["id"]:
            # yes, let's add to people list
            movie["people"].append(person["name"])


def get_json_request(url, *args, **kwargs):
    """
    Auxiliary function to obtain the json from get request response.
    :param url:
    :return: json response
    """
    try:
        response = requests.get(url, timeout=10)
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.warning(e)
        return []
