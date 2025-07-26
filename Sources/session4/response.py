import random

def get_res(user_in):
    for key in responses:
        if key in user_in:
            return random.choice(responses[key])
    return random.choice(responses["default"])