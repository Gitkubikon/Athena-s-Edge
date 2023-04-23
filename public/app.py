import asyncio
from scrape import getPopularHackerNewsPosts 
import openai
import os

previous_posts = []

async def main():
    while True:
        new_posts = await getPopularHackerNewsPosts()
        for post in new_posts:
            if post not in previous_posts:
                print(post.title, post.points)
                # generate_article(post)
                previous_posts.append(post)
        await asyncio.sleep(100)

def generate_article(post, model_engine="davinci", temperature=0.5, max_tokens=1024):
    # Set up OpenAI API credentials
    openai.api_key = os.environ["OPENAI_API_KEY"]
    
    # Set up parameters for the API call
    prompt = f"Generate article for post: {post.title}."
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    
    # Get the generated text from the API response
    message = completions.choices[0].text
    
    return message

if __name__ == '__main__':
    asyncio.run(main())
