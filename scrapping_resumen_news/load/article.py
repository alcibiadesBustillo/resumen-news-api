from sqlalchemy import Column, String, Integer

from base import Base

class Article(Base):
    __tablename__ = 'news_news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String)
    title = Column(String)
    body = Column(String)
    url = Column(String)
    newspaper_uid = Column(String)
    host = Column(String)   
    

    def __init__(self,                    
                    uid,
                    title,
                    body,
                    url,
                    newspaper_uid,                   
                    host):
        self.uid = uid         
        self.body = body
        self.host = host
        self.title = title
        self.newspaper_uid = newspaper_uid         
        self.url = url       