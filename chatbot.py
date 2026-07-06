"""A simple chtatbot that responds to user input based on predefined rules."""


def get_response(user_input):
    """Takes user input and returns a predefined reply based on matching rules."""
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text in ("how are you", "how are you?"):
        return "I'm fine, thanks! How about you?"
    elif text in ("what is your name", "what's your name", "who are you"):
        return "I'm a simple rule-based chatbot."
    elif text in ("help", "what can you do"):
        return "You can say things like: hello, how are you, your name, or bye."
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."

def chat():
    """Runs the main chatbot loop, taking input until the user says bye/exit/quit."""
    print("Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chat()