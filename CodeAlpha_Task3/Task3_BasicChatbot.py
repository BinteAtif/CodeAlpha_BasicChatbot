import random
from datetime import datetime

def get_response(user_input, name):
    user_input = user_input.strip().lower()
    
    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey", "sup"]):
        responses = ["Hi there!", "Hello! Nice to see you.", "Hey! How's it going?"]
        return random.choice(responses)
    
    # How are you
    elif "how are you" in user_input or "how r u" in user_input:
        responses = ["I'm doing great, thanks!", "Feeling chatbot-tastic!", "I'm fine, how about you?"]
        return random.choice(responses)
    
    # Name related
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm GrokBot, a simple rule-based chatbot!"
    elif "my name is" in user_input:
        new_name = user_input.split("my name is")[-1].strip().title()
        return f"Nice to meet you, {new_name}! I'll remember that."
    
    # Time
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    
    # Joke
    elif "joke" in user_input or "funny" in user_input:
        jokes = [
            "Why don't skeletons fight each other? They don't have the guts!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I'm reading a book about anti-gravity. It's impossible to put down!"
        ]
        return random.choice(jokes)
    
    # Weather
    elif "weather" in user_input:
        return "I'm just a chatbot, I can't check real weather, but I hope it's sunny where you are! ☀️"
    
    # Age
    elif "how old are you" in user_input or "your age" in user_input:
        return "I'm a timeless chatbot — just a few lines of code old!"
    
    # Favorite color
    elif "favorite color" in user_input:
        return "I love blue — it reminds me of the sky and clean code!"
    
    # Goodbye
    elif any(word in user_input for word in ["bye", "goodbye", "see you", "exit", "quit"]):
        return "Goodbye! It was nice chatting with you. Have a great day! 👋"
    
    # Help
    elif "help" in user_input or "what can you do" in user_input:
        return """I can talk about:
• Greetings (hi, hello)
• Time
• Jokes
• Weather
• My name / your name
• My favorite color
Just type 'bye' to exit!"""
    
    else:
        return "Sorry, I didn't understand that. Try saying 'help' to see what I can do!"

def simple_chatbot():
    print("🤖 Welcome to GrokBot!")
    print("Type 'help' to see what I can do. Type 'bye' to exit.\n")
    
    user_name = None
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
            
        # Check for name
        if "my name is" in user_input.lower():
            user_name = user_input.split("my name is")[-1].strip().title()
        
        response = get_response(user_input, user_name)
        print(f"Chatbot: {response}")
        
        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"]):
            break

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()