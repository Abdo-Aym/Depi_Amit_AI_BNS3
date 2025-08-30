import random
import json
import random
# Load responses from the JSON file
with open("G:/DEPI/Depi_Amit_AI_BNS3/Sources/session4/chatbot.json", "r") as file:
    responses = json.load(file)
    # print(responses)
class Bot:
    def __init__(self, user_input):
        self.user_input= user_input
    # Function to get a response based on user input
    def get_response(self):
        for key in responses:
            if key in self.user_input:
                return random.choice(responses[key])
       
        return random.choice(responses["default"])