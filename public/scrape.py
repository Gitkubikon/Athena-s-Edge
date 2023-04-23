import aiohttp
import asyncio
from typing import List


class HackerNewsPost:
    def __init__(self, title: str, points: int):
        self.title = title
        self.points = points


async def getPopularHackerNewsPosts() -> List[HackerNewsPost]:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get('https://hacker-news.firebaseio.com/v0/topstories.json') as response:
                storyIds = await response.json()

            topStories = storyIds[:10]
            storyPromises = [session.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json') for id in topStories]

            responses = await asyncio.gather(*storyPromises)
            stories = [await response.json() for response in responses]

            return [HackerNewsPost(story['title'], story['score']) for story in stories]

        except aiohttp.ClientError as e:
            print(e)
            return []
