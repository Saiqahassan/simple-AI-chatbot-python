import random

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi, there!",
    "how are you": "I'm doing well, thank you for asking!",
    "who are you": "I'm a chatbot!",
    "what can you do": "I can help you with a variety of things, just ask!",
    "bye": "Goodbye! Have a great day!",
}
def chatbot():
    print("Welcome to the chatbot!\n")
    print("----------------------\n")
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Chatbot:", responses[user_input])
        else:
            print("Chatbot: I'm sorry, I don't understand.")

        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break

chatbot()