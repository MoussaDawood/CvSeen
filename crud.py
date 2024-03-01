from sqlalchemy.orm import Session
import models
from auxiliary import generate_random_ascii_string
from fastapi import HTTPException, status



def increment_requests_num_by_one(original_url,db:Session):
    original_url.num_requested=original_url.num_requested+1
    db.commit()
    db.refresh(original_url)

def get_short_url(db: Session, original_url):
    return db.query(models.ShortUrl).filter(models.ShortUrl.original_url == original_url).first()

def get_original_url(db: Session, short_url_uid):
    original_url = db.query(models.ShortUrl).filter(models.ShortUrl.short_url_uid == short_url_uid).first()
    if original_url == None : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no url paired with this short url")
    return original_url

def insert_long_short_url_row(db:Session,original_url):
    url_short_long_row = models.ShortUrl(original_url   = original_url.url,
                                         short_url_uid  = generate_random_ascii_string(12),
                                         cv_title       = original_url.cv_title)

    db.add(url_short_long_row)
    db.commit()
    db.refresh(url_short_long_row)
    return url_short_long_row.short_url_uid

        
            
            
            
