from response import Bot

if __name__ == "__main__":
    print('Chatbot: Hi! How can I assist you today?')
    while True:
        user_in = input('User: ').lower()
        bot = Bot(user_in)
        print('Chatbot: ', bot.get_response())
        if user_in == 'goodbye':
            break