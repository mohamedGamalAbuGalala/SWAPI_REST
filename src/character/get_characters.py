import asyncio
from character.utils import fetch
from character.get_character import get_character

SWAPI_BASE = 'https://swapi.dev/api/'


async def get_characters(search):
    data = await fetch(f'{SWAPI_BASE}people/?search={search}')

    fetch_results = data['results']

    if(len(fetch_results) == 0):
        return False

    #  We can enable this step, but it will give us timeout Error cuz the timeout is only 10 s
    #           And in fact 10 matched results is enough for search feature.
    #           If you need to get all we can do pagination in our search API itself

    # while data['next']:
    #     data = await fetch(data['next'])
    #     newRes = fetch_results + data['results']
    #     if(len(newRes) == 0):
    #         break
    #     fetch_results = newRes

    futures = [get_character(item) for item in fetch_results]

    result = await asyncio.gather(
        *futures
    )

    return result
