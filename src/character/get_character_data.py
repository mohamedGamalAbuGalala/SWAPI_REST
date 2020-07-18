import asyncio
from character.utils import fetch


async def get_species(species_urls):
    futures = [fetch(url) for url in species_urls]

    result = await asyncio.gather(
        *futures
    )

    species_return = []

    for item in result:
        species_return.append({
            'name': item['name'],
            'averageLifespan': item['average_lifespan']
        })

    return species_return


async def get_home_planet(home_world_url):
    futures = [fetch(home_world_url)]

    result = await asyncio.gather(
        *futures
    )

    home_planet_return = 'Homeless 😢'

    if(len(result) != 0):
        home_planet_return = result[0]['name']

    return home_planet_return


async def get_movies(movies_urls):
    futures = [fetch(url) for url in movies_urls]

    result = await asyncio.gather(
        *futures
    )

    movies_return = []

    for item in result:
        movies_return.append(item['title'])

    return movies_return
