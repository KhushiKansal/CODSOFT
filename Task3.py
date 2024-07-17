# Chatbot

import random

class RuleBasedChatbot:
    def _init_(self):
        self.responses = {
    "hello": ["Hello!", "Hi there!", "Hey!", "Hi!", "Greetings!", "Hey, how's it going?", "Hiya!", "Hey there!", "Hello, how can I assist you?", "Hey! What's up?", "Hello, nice to meet you!", "Hey, how are you doing?"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, thanks for asking.", "I'm doing great!", "I'm okay, how about you?", "I'm feeling fantastic!", "I'm doing alright.", "I'm fabulous, thanks for asking!", "I'm splendid, thanks!", "I'm wonderful, how about yourself?", "I'm pretty good, thanks for asking.", "I'm great, thanks!", "I'm fantastic, how about you?", "I'm doing just fine, thanks!", "I'm doing awesome, thank you for asking!", "I'm peachy, thanks!"],
    "what's your name": ["I'm just a chatbot.", "You can call me ChatBot.", "I don't really have a name, but you can call me ChatBot.", "I'm your friendly chatbot assistant!", "I go by ChatBot.", "I'm a virtual assistant designed to help you!", "I'm a bot programmed to assist you.", "I'm your AI companion, here to help!", "I'm your digital friend, ChatBot!", "My name is ChatBot, nice to meet you!", "You can refer to me as ChatBot, how can I assist you today?", "I'm your friendly neighborhood ChatBot!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!", "Farewell!", "Catch you later!", "Take care!", "Until next time!", "Bye for now!", "Goodbye, it was nice chatting with you!", "Adios!", "So long!", "Until we meet again!", "Bye-bye!", "Peace out!", "Later, gator!", "Take it easy!", "Keep in touch!", "Bye now, have a good one!", "Bye, take care of yourself!"],
    "thank you": ["You're welcome!", "No problem!", "Anytime!", "Glad I could help!", "Don't mention it!", "Happy to assist!", "My pleasure!", "It was my pleasure to help!", "You're welcome, feel free to ask anytime!", "No worries!", "Not a problem!", "It's all good!", "You're welcome, have a great day!", "No trouble at all!"],
    "good morning": ["Good morning!", "Morning!", "Hey, good morning!", "Good morning! How are you?", "Rise and shine!", "Top of the morning to you!", "Good morning! Have a great day!", "Morning! What's on your agenda today?", "Hey there! Good morning to you!", "Good morning! How's the coffee?", "Morning! How's the weather where you are?", "Morning! Any plans for the day?"],
    "good afternoon": ["Good afternoon!", "Afternoon!", "Hey, good afternoon!", "Good afternoon! How's your day going?", "Afternoon! How can I help you?", "Hey there! Good afternoon to you!", "Good afternoon! What's on your mind?", "Hello! How's your afternoon?", "Hey, afternoon!", "Good afternoon! Enjoying the day?"],
    "good evening": ["Good evening!", "Evening!", "Hey, good evening!", "Good evening! How was your day?", "Evening! How can I assist you?", "Hey there! Good evening to you!", "Good evening! What's going on?", "Hello! How's your evening?", "Hey, evening!", "Good evening! Ready to unwind?"],
    "sorry": ["It's okay.", "No worries.", "That's alright.", "Don't worry about it.", "Apology accepted.", "No problem.", "It happens.", "No need to apologize.", "It's all good.", "I understand."],
    "how's it going": ["It's going well, thank you for asking!", "Things are going smoothly, how about you?", "I'm doing great, thanks for asking!", "Everything's going fine, thanks!", "Things are going well here, how about yourself?", "It's going good, thanks!", "I'm having a good day so far, thanks!", "I'm doing well, thanks for asking!"],
    "what can you do": ["I can provide information, answer questions, and assist you with various tasks.", "I can engage in conversations, offer advice, and entertain you.", "I can help you with tasks, provide recommendations, and offer support.", "I'm here to chat, assist, and keep you company!", "I can assist you with a wide range of tasks, just let me know what you need.", "I'm capable of answering questions, providing information, and offering assistance.", "I can provide useful information, engage in conversations, and even tell jokes!", "I'm equipped to help you with a variety of tasks, from answering questions to providing recommendations.", "I'm designed to assist you with anything you need help with, just ask!", "I can assist you with queries, tasks, and provide useful information.", "I'm here to assist you in any way I can, just let me know what you need help with.", "I'm capable of providing information, offering advice, and engaging in conversations."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!", "Why don't skeletons fight each other? They don't have the guts!", "I told my wife she was drawing her eyebrows too high. She looked surprised!", "What do you get when you cross a snowman and a vampire? Frostbite!"],
    
    "tell me a fact": ["The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion of the metal.", "A flock of crows is known as a murder"]
 }

    def respond(self, message):
        message = message.lower()
        for key in self.responses:
            if key in message:
                return random.choice(self.responses[key])
        return "I'm sorry, I don't understand that."

def main():
    chatbot = RuleBasedChatbot()
    print("Welcome to the Rule-Based Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot.respond(user_input))
            break
        else:
            print("ChatBot:", chatbot.respond(user_input))

if _name_ == "_main_":
    main()
