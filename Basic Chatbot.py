import nltk
from nltk.chat.util import Chat, reflections
from nltk.sentiment.vader import SentimentIntensityAnalyzer

pairs = [
    [
        r"Hi my name is (.*)",
        ["Nice to meet you, %1! How can I assist you today?",]
    ],
    [
        r"what is your name?",
        ["I'm Chatbot, your virtual assistant. How can I help you today?",]
    ],
    [
        r"how are you?",
        ["I'm just a bunch of code, but I'm feeling great! How about you?",]
    ],
    [
        r"what do you do?",
        ["I can chat with you, provide information, and help answer your questions!",]
    ],
    [
        r"can you help me with (.*)?",
        ["I'd be happy to help with %1! What specifically do you need assistance with?",]
    ],
    [
        r"thank you",
        ["You're welcome! Is there anything else I can do for you?",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",]
    ],
    [
        r"i\'m feeling (.*)",
        ["I'm sorry to hear that you're feeling %1. Is there anything I can do to cheer you up?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?",]
    ],
    [
        r"what is your purpose?",
        ["My purpose is to assist you and make your day a little easier. How can I help?",]
    ],
    [
        r"tell me about yourself",
        ["I'm an AI chatbot designed to assist you with various tasks and provide information. What would you like to know?",]
    ],
    [
        r"goodbye|bye",
        ["Goodbye! Have a great day!", "See you later! Take care!",]
    ],
    [
        r"how is the weather in (.*)?",
        ["I don't have real-time weather data, but I can tell you that the weather in %1 is usually quite interesting!",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am based in the digital world, but I can talk about any place you'd like!",]
    ],
    [
        r"(.*) hobbies?",
        ["I enjoy learning new things and chatting with people like you!",]
    ],
]

def chatbot():
    print("Chatbot : Hi! I'm Chatbot. How can I help you today?")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("you :").strip()
        if user_input.lower() == 'quit':
            print("Chatbot : Bye, take care. See you soon!")  
            break
        response = chat.respond(user_input)
        print("Chatbot :", response)

if __name__ == "__main__":
    nltk.download('vader_lexicon')
    chatbot()