import os
import json
from toolhouse import Toolhouse
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# 👋 Make sure you've also installed the Together SDK through: pip install together
from together import Together 

# Get the Together API key from environment variables
together_api_key = os.getenv('TOGETHER_API_KEY')

# Initialize Together client using the API key
client = Together(api_key=together_api_key)
MODEL = 'mistralai/Mixtral-8x7B-Instruct-v0.1'

# Initialize Toolhouse client
th = Toolhouse(access_token=os.getenv('TOOLHOUSE_API_KEY'))

messages = [{
    "role": "user",
    "content":
        "Generate Two Sum code."
        "Make the two arguements array called nums=[2,7,11,15] and target=9."
        "After posting the code, give a basic explination on how the code works"
}]

# Get the initial response from Together
response = client.chat.completions.create(
  model=MODEL,
  messages=messages,
  tools=th.get_tools(),  # Pass Code Execution as a tool
)

# Debug: Print the response to inspect its structure
print("Response from Together:", response)

# Extract the content from the response
if response.choices and response.choices[0].message.content:
    content = response.choices[0].message.content
    print("Extracted content:\n", content)
else:
    print("No content found in the response.")
