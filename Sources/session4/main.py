import json
with open("G:/DEPI/Depi_Amit_AI_BNS3/Sources/session4/chatbot.json","r") as file:
    responses = json.load(file)
from response import get_res

if __name__ == "__main__":
    print('Chatbot: Hi! How can I assist you today?')
    while True:
        user_in = input('User: ').lower()
        response = get_res(user_in)
        print('Chatbot: ', response)
        if user_in == 'goodbye':
            break