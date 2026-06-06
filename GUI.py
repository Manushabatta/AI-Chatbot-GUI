import tkinter as tk
from tkinter import scrolledtext

def get_response(user):
    user = user.lower()

    if user == "bye":
        return "Goodbye! Have a nice day."

    elif "hello" in user or "hi" in user:
        return "Hello! How can I help you?"

    elif "name" in user:
        return "My name is AI Chatbot."

    elif "java" in user:
        return "Java is an object-oriented programming language."

    elif "python" in user:
        return "Python is widely used in AI, web development, and automation."

    elif "html" in user:
        return "HTML is used to create web pages."

    elif "css" in user:
        return "CSS is used to style web pages."

    elif "javascript" in user:
        return "JavaScript adds interactivity to websites."

    elif "thank" in user:
        return "You're welcome!"

    elif "ai" in user:
        return "AI stands for Artificial Intelligence."

    else:
        return "Sorry, I don't understand that question."

def send_message():
    user_message = entry.get().strip()

    if user_message == "":
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, "You: " + user_message + "\n")

    bot_response = get_response(user_message)

    chat_area.insert(tk.END, "Bot: " + bot_response + "\n\n")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    entry.delete(0, tk.END)

    if user_message.lower() == "bye":
        root.after(1000, root.destroy)

def send_on_enter(event):
    send_message()

# Main Window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("600x500")

# Heading
title_label = tk.Label(
    root,
    text="AI Chatbot",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

# Chat Area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=65,
    height=20,
    state=tk.DISABLED
)
chat_area.pack(padx=10, pady=10)

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

entry = tk.Entry(
    input_frame,
    width=45,
    font=("Arial", 12)
)
entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    width=10
)
send_button.pack(side=tk.LEFT)

entry.bind("<Return>", send_on_enter)

# Welcome Message
chat_area.config(state=tk.NORMAL)
chat_area.insert(
    tk.END,
    "Bot: Hello! I am your AI Chatbot.\nType your message below.\n\n"
)
chat_area.config(state=tk.DISABLED)

root.mainloop()