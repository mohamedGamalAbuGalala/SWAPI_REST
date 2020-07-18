import async_timeout
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session, async_timeout.timeout(10):
        async with session.get(url) as response:
            assert response.status == 200
            return await response.json()
