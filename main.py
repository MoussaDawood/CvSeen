from fastapi import FastAPI
from telegram import Bot


Telegrm_Token = 'YOUR_TOKEN'
# Replace 'CHAT_ID' with the chat ID of the recipient
# You can obtain it by sending a message to your bot and then fetching it from the received message object
# Alternatively, you can use your own chat ID for testing purposes
Telegram_group = 'YOUR_CHAT_ID'
app = FastAPI()



@app.get('/')
def root():
    pass


def send_message(chat_id, message):
    bot = Bot(token=Telegrm_Token)
    bot.send_message(chat_id=chat_id, text=message)


def get_cv_title():
    # TODO:
    return 'CV_TITLE'



@app.get('/')
def short_url_request(id:str):    
    cv_title = get_cv_title(id)
    message_text = f"Cv with title : {cv_title} is opened"
    send_message(Telegram_group, message_text)
    

if __name__ == "__main__":
    pass