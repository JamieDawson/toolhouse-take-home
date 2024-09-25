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



# id='8c8079aefe64ceed-SJC' object=<ObjectType.ChatCompletion: 'chat.completion'> created=1727156803 model='mistralai/Mixtral-8x7B-Instruct-v0.1' choices=[ChatCompletionChoicesData(index=0, logprobs=None, seed=8867901209696889000, finish_reason=<FinishReason.EOS: 'eos'>, message=ChatCompletionMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content=' Sure, I can help with that. Here\'s the FizzBuzz code in Python:\n\n```python\nfor i in range(1, 101):\n    if i % 3 == 0 and i % 5 == 0:\n        print("FizzBuzz")\n    elif i % 3 == 0:\n        print("Fizz")\n    elif i % 5 == 0:\n        print("Buzz")\n    else:\n        print(i)\n```\n\nThis code uses a for loop to iterate from 1 to 100. For each number, it checks if it is divisible by both 3 and 5 (i % 3 == 0 and i % 5 == 0), divisible by 3 (i % 3 == 0), or divisible by 5 (i % 5 == 0). If it is divisible by both 3 and 5, it prints "FizzBuzz". If it is divisible by 3, it prints "Fizz". If it is divisible by 5, it prints "Buzz". If it is not divisible by either 3 or 5, it prints the number itself.\n\nThe code works by using the modulus operator (%) to check if a number is divisible by another number. If a number is divisible by another number, the remainder will be 0. So, if i % 3 == 0, it means that i is divisible by 3. Similarly, if i % 5 == 0, it means that i is divisible by 5.\n\nI hope this helps! Let me know 
# if you have any further questions.', tool_calls=[]))] prompt=[] usage=UsageData(prompt_tokens=2238, completion_tokens=374, total_tokens=2612)


#Give me a description of how FizzBuzz works and then show me some code
#This command calls content!

# id='8c807fd2586667be-SJC' object=<ObjectType.ChatCompletion: 'chat.completion'> created=1727157054 model='mistralai/Mixtral-8x7B-Instruct-v0.1' choices=[ChatCompletionChoicesData(index=0, logprobs=None, seed=15379814100009253000, finish_reason=<FinishReason.EOS: 'eos'>, message=ChatCompletionMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content=' Sure, I can help with that. FizzBuzz is a simple programming task where you have to print numbers from 1 to 
# 100, but for multiples of three, you print "Fizz" instead of the number, and for multiples of five, you print "Buzz". For numbers which are multiples of both three and five, you print "FizzBuzz".\n\nHere\'s a simple Python code that does this:\n\n```python\nfor i in range(1, 101):\n    if i % 3 == 0 and i % 5 == 0:\n        print("FizzBuzz")\n    elif i % 3 == 0:\n        print("Fizz")\n    elif i % 5 == 0:\n        print("Buzz")\n    else:\n        print(i)\n```\n\nThis code uses a for loop to iterate over the numbers from 1 to 100. It then uses if-elif-else statements to check if the current number is divisible by 3, 5, or both. If it\'s divisible by both, it prints "FizzBuzz", if it\'s only divisible by 3, it prints "Fizz", if it\'s only divisible by 5, it 
# prints "Buzz", and if it\'s not divisible by either, it just prints the number itself.', tool_calls=[]))] prompt=[] usage=UsageData(prompt_tokens=2230, completion_tokens=312, total_tokens=2542)



## Generate FizzBuzz code. Execute it to show me the results up to 10.
# This command calls tool_call!



##