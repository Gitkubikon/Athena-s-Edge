import openai
import json
import os

# Set your OpenAI API key
openai.api_key = "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"

# Define the path to the metadata file
metadata_file = "./content/metadata.json"

# Define the path to the content directory
content_dir = "./content"

# Load the metadata file
with open(metadata_file, "r") as f:
    metadata = json.load(f)

# Loop through the articles in the metadata file
for filename, info in metadata.items():
    # Define the path to the article file
    filepath = os.path.join(content_dir, info["main_tag"], filename)

    # Check if the article file exists
    if not os.path.exists(filepath):
        # If the article file does not exist, print an error message
        print(f"Error: {filepath} does not exist")
        continue

    # Read the article file
    with open(filepath, "r") as f:
        article = f.read()

    # Call the OpenAI API to categorize the article
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Categorize the article:\n{article}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the category tags from the OpenAI API response
    tags = response["choices"][0]["text"].strip().split(",")
    tags = [tag.strip() for tag in tags]

    # Set the tags and main_tag values in the metadata file
    info["tags"] = tags
    info["main_tag"] = os.path.basename(os.path.dirname(filepath))

    # Write the updated metadata file
    with open(metadata_file, "w") as f:
        json.dump(metadata, f)

    # Move the article file to the new directory based on the main_tag value
    new_dir = os.path.join(content_dir, info["main_tag"])
    os.makedirs(new_dir, exist_ok=True)
    os.rename(filepath, os.path.join(new_dir, filename))

    # Log the tags and main_tag
    print(f"{filename} categorized as {', '.join(tags)} and moved to {new_dir}")
