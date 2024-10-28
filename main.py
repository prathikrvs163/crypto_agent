from llama_agent import call_llama
from crypto_price import fetch_crypto_price
from translation import translate_to_english

# Store conversation history for context management
conversation_history = []

def append_to_history(user_message, bot_response):
    """Store the last 5 interactions."""
    conversation_history.append(f"User: {user_message}")
    conversation_history.append(f"Agent: {bot_response}")

    # Keep only the last 5 messages
    if len(conversation_history) > 10:
        conversation_history.pop(0)

def get_conversation_history():
    """Retrieve the last 5 messages."""
    return "\n".join(conversation_history)

def handle_user_input(user_input):
    """Process user input and call the appropriate function."""
    if "price" in user_input.lower():
        # Extract the cryptocurrency name from the user's query
        crypto_name = user_input.lower().replace("price", "").strip()
        response = fetch_crypto_price(crypto_name if crypto_name else "bitcoin")
    elif "translate:" in user_input.lower():
        # Handle translation requests
        text_to_translate = user_input.split(":", 1)[1].strip()
        response = translate_to_english(text_to_translate)
    else:
        # Use LLaMA model to handle general questions
        prompt = get_conversation_history() + f"\nUser: {user_input}\nAgent:"
        response = call_llama(prompt)

    append_to_history(user_input, response)
    return response

def run_agent():
    """Main loop to interact with the user."""
    print("Welcome to the Crypto AI Agent! Ask about any cryptocurrency prices or request translations.")
    while True:
        user_message = input("You: ")
        if user_message.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        bot_response = handle_user_input(user_message)
        print(f"Agent: {bot_response}")

if __name__ == "__main__":
    run_agent()
