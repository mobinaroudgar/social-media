from model.entity.base import Base
from sqlalchemy import Integer,String,Column

class Post(Base):
    __tablename__ = "post_tbl"

    id = Column(Integer,primary_key=True)
    text=Column(String(30))

    def __init__(self, id, text):
        self.id = id
        self.text = text
        #self.image=image
        #self.date_time = date_time

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())
