import openai

# Initialize the OpenAI client with your API key
openai.api_key = "Api key"

# Create a completion request
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Ensure the model name is correct
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Cloud with creative flair."},
        {"role": "user", "content": "What is coding?"}
    ]
)

# Print the response
print(response.choices[0].message['content'])

