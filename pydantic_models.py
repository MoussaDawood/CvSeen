from pydantic import BaseModel


class OriginalUrl(BaseModel):
    url : str = "http://google.com"
    cv_title : str 
    
    
# class UrlLongShortRow(BaseModel):
#     original_url : str
#     short_url_uid: str
 
        