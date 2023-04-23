import openai
import re
openai.api_key = "YOUR_API_KEY"

def generate_article(heading):
    # Clean the input heading
    cleaned_heading = re.sub('[^a-zA-Z0-9\n\.]', ' ', heading)
    
    # Set up the prompt
    prompt = f"Write an article on the topic: {cleaned_heading}\n\n"
    
    # Generate the article using GPT-3
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.7,
      max_tokens=1000,
      n_context=1
    )
    article = response.choices[0].text
    
    return article
