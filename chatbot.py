def chatbot():
    print("=== AI Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("Bot: Goodbye!")
            break

        elif "hello" in user or "hi" in user:
            print("Bot: Hello! How can I help you?")

        elif "name" in user:
            print("Bot: My name is AI Chatbot.")

        elif "java" in user:
            print("Bot: Java is an object-oriented programming language.")

        elif "python" in user:
            print("Bot: Python is a versatile programming language used in AI, web development, and more.")

        elif "html" in user:
            print("Bot: HTML is used to create web pages.")

        elif "css" in user:
            print("Bot: CSS is used to style web pages.")

        elif "javascript" in user:
            print("Bot: JavaScript adds interactivity to websites.")

        elif "thank" in user:
            print("Bot: You're welcome!")

        else:
            print("Bot: Sorry, I don't understand that question.")

chatbot()