import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize the client with your key
client = genai.Client(api_key=os.getenv("AIzaSyBzgM7qQB32xZWlxG7-1jNs309FHIzvLiY"))

print("Listing models supported by your API key:\n")

# Iterate through available models
for m in client.models.list():
    # Only list models that support text generation
    if "generateContent" in m.supported_actions:
        print(f"Model Name: {m.name}")
        print(f"Display Name: {m.display_name}")
        print("-" * 30)