import random

# Define responses to user input
greetings = ["hello", "hi", "hey", "greetings", "yo"]
responses = ["Hello!", "Hi there!", "Greetings!", "Hey! How can I help you?", "Yo! What's up?"]

# Define function for responding to user input
def respond(input):
    if input.lower() in greetings:
        return random.choice(responses)
    else:
        return "I'm sorry, I don't understand. Can you rephrase that?"

# Main program loop
while True:
    user_input = input("You: ")
    bot_response = respond(user_input)
    print("Bot: " + bot_response)
