from sqlalchemy import  Column, String, Integer
from database import Base


class ShortUrl(Base):
    __tablename__ = "short_urls"

    # id = Column(Integer, primary_key=True)
    short_url_uid = Column(String, index=True ,primary_key=True)
    original_url  = Column(String)
    cv_title      = Column(String)
    num_requested = Column(Integer,default=0)
    
    