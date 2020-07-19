import asyncio
from src.character.get_character_data import *


async def get_character(character):
    data_promises = await asyncio.gather(
        get_species(character['species']),
        get_home_planet(character['homeworld']),
        get_movies(character['films']),
    )

    species = data_promises[0]       # array
    home_planet = data_promises[1]    # item
    movies = data_promises[2]        # array

    character = {
        'fullName': character['name'],
        'gender': character['gender'],
        'species': species,
        'homePlanet': home_planet,
        'movies': movies
    }

    return character
