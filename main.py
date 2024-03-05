from fastapi import FastAPI, HTTPException, status, Depends,Request
from fastapi.responses import RedirectResponse
from auxiliary import *
import pydantic_models
from auxiliary import generate_random_ascii_string
import validators
from sqlalchemy.orm import Session
import crud
import models
import pydantic_models
from database import SessionLocal, engine
from  mangum import Mangum

app = FastAPI()
handler = Mangum(app)
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


'''
post msgs with original url then 
    - generate unique id and ensures that it is unique
    - set the new id to DB and point to the original url and title
    - respond to the post request with the new urls
'''



@app.post("/get_url_with_id")
def create_short_url(request: Request,
                     original_url: pydantic_models.OriginalUrl,
                     db: Session = Depends(get_db)):

    # if not valid url raise error
    if not validators.url(original_url.url):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Not a valid url")

    short_url_id = crud.insert_long_short_url_row(
        db=db, original_url=original_url)
    return {
        "title": original_url.cv_title,
        "original_url": original_url.url,
        "short_url": str(request.base_url)+short_url_id
    }


'''
when short url requested then
    - query the DB for the orginal url
    - query the Db for the title of orignal url
    - send msg via telegram that cv with TITLE open
    - 301 th request to the original url
'''


@app.get("/{short_url_uid}")
def surf_short_url(short_url_uid: str, db: Session = Depends(get_db)):
    # get the original url db row
    original_url = crud.get_original_url(short_url_uid=short_url_uid, db=db)

    # send message on telegram
    message_text = \
        f"Cv with title : {original_url.cv_title} is opened"
    send_message(bot_token, chat_id, message_text)

    # save the number of url requests to databse
    crud.increment_requests_num_by_one(original_url, db)

    # 301 to original url
    return RedirectResponse(url=original_url.original_url, status_code=301)


# # if __name__ == "__main__":
# #     uvicorn.run("main:app",host="127.0.0.1",port=8000)
