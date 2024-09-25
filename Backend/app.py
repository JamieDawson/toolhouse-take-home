from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from toolhouse import Toolhouse
from dotenv import load_dotenv
from together import Together 
# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the frontend

# Load environment variables from the .env file
load_dotenv()

# Get the Together API key from environment variables
together_api_key = os.getenv('TOGETHER_API_KEY')

# Initialize Together client using the API key
client = Together(api_key=together_api_key)
MODEL = 'mistralai/Mixtral-8x7B-Instruct-v0.1'

# Initialize Toolhouse client
th = Toolhouse(access_token=os.getenv('TOOLHOUSE_API_KEY'))

#STARTING HERE
@app.route('/generate-code', methods=['POST'])
def generate_code():
    data = request.get_json()
    user_content = data.get('content', '')

    # Modify the messages object with the content received from the frontend
    messages = [{
        "role": "user",
        "content": user_content
    }]

#STARTING HERE

    try:
        # Get the initial response from Together
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=th.get_tools(),
        )

        print(response)

        # Check if there is a tool call in the response
        if response.choices and response.choices[0].message.tool_calls:
            tool_call = response.choices[0].message.tool_calls[0]
            # Extract the code from the tool_call arguments
            function_arguments = tool_call.function.arguments
            return jsonify({"tool_call_code": function_arguments})
        
        # If no tool call, check for content (although it seems to be absent)
        elif response.choices and response.choices[0].message.content:
            content = response.choices[0].message.content
            return jsonify({"response": content})
        
        else:
            return jsonify({"error": "No content or tool call found in the response."}), 400

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to generate a response from Together API."}), 500


if __name__ == '__main__':
    app.run(debug=True)
