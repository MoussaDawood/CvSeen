import requests

# get it from @BotFather
TelegramToken = 'YOUR_TOKEN_HERE'


def get_chat_id():
    response = requests.get(
        f'https://api.telegram.org/bot{TelegramToken}/getUpdates')
    data = response.json()
    if data['ok']:
        # Get the latest message
        latest_message = data['result'][-1]
        # Get the chat ID from the latest message
        chat_id = latest_message['message']['chat']['id']
        # print(latest_message,"666")

        return chat_id
    else:
        # print("Error occurred while fetching updates:", data['description'])
        return None


if __name__ == "__main__":
    # send msg to your telegram bot first ex: /start
    chat_id = get_chat_id()
    if chat_id:
        print("Chat ID:", chat_id)
    else:
        print("Failed to retrieve the chat ID.")
