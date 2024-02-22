from fastapi import FastAPI
import uvicorn
from methods import *


app = FastAPI()


'''
post msgs with original url then 
    - generate unique id and ensures that it is unique
    - set the new id to DB and point to the original url and title
    - respond to the post request with the new urls

'''
@app.post("/get_url_with_id")
def get_url_with_id():
    pass




'''
when short url requested then
    - query the DB for the orginal url
    - query the Db for the title of orignal url
    - send msg via telegram that cv with TITLE open
    - 301 th request to the original url
'''     
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