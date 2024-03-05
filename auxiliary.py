import requests
import random
import string


# get it from @BotFather
bot_token = '7089629432:AAEX9ts73EvYmte66oHMh2v52xvyok2XYCw'
# get it from getchatid.py
chat_id = '566639260'


def generate_random_ascii_string(length):
    ascii_characters = string.ascii_letters + string.digits
    random_string = ''
    for _ in range(length):
        random_string += random.choice(ascii_characters)
    return random_string


def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Failed to send message. Error: {response.text}")


def get_original_url(id):
    return "https://google.com"


def redirect_to_original(original_url):
    pass
