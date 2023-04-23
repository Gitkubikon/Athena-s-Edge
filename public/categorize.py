import openai
import json
import os

# Set up OpenAI API credentials
openai.api_key = "INSERT_YOUR_API_KEY_HERE"

# Load metadata.json file or create new dictionary
if os.path.exists("content/metadata.json"):
    with open("content/metadata.json", "r") as f:
        metadata = json.load(f)
else:
    metadata = {"unindexed": {}}

# Create "unindexed" key in metadata dictionary if it doesn't exist
if "unindexed" not in metadata:
    metadata["unindexed"] = {}

# Loop through files in unindexed directory
for article in os.listdir("content/unindexed"):
    # Check if file is a directory
    if os.path.isdir(os.path.join("content/unindexed", article)):
        # Load index.md file for article
        with open(os.path.join("content/unindexed", article, "index.md"), "r") as f:
            content = f.read()

        # Prompt OpenAI API to extract categories from article content
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Extract categories from the following article:\n{content}\n\nCategories:",
            max_tokens=1024,
            n=1,
            stop="Categories:",
            temperature=0.7,
        )

        # Extract categories from OpenAI API response
        categories = [c["text"].strip() for c in response.choices[0].text.split("\n") if c["text"].strip()]

        # Update metadata.json file with categories for article
        metadata["unindexed"][article] = {"categories": categories}

# Save updated metadata.json file
with open("content/metadata.json", "w") as f:
    json.dump(metadata, f, indent=4)
