def chatbot():
    print("Welcome to QuickHelp Customer Support!")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I assist you today?")

        elif "hours" in user_input or "timing" in user_input:
            print("Bot: We are open from 9 AM to 6 PM, Monday to Saturday.")

        elif "price" in user_input or "cost" in user_input:
            print("Bot: Our pricing starts at ₹499. Would you like a detailed quote?")

        elif "location" in user_input or "address" in user_input:
            print("Bot: We are located at MG Road, Pune.")

        elif "exit" in user_input:
            print("Bot: Thank you for chatting with us. Have a great day!")
            break

        else:
            print("Bot: I'm sorry, I didn't understand that. Could you please rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
