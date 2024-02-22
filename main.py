from fastapi import FastAPI
import requests
import uvicorn

# get it from @BotFather
bot_token = '7089629432:AAEX9ts73EvYmte66oHMh2v52xvyok2XYCw'
# get it from getchatid.py
chat_id = '566639260'


app = FastAPI()


def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Error: {response.text}")


def get_cv_title(id):
    # TODO:
    return 'CV_TITLE'


def get_original_url(id):
    return "https://google.com"
    
    
def redirect_to_original(original_url):
    pass
    
    
@app.get('/')
def short_url_request(id:str):    
    
    # send message on telegram 
    cv_title = get_cv_title(id)
    message_text = f"Cv with title : {cv_title} is opened"
    send_message(bot_token,chat_id, message_text)

    
    # 301 to the actual location 
    original_url = get_original_url(id)
    redirect_to_original(original_url)
    # save click in sql database
    pass



# if __name__ == "__main__":
#     uvicorn.run("main:app",host="127.0.0.1",port=8000)