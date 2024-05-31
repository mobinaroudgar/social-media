from datetime import datetime

from sqlalchemy.orm import relationship
from model.entity.base import Base
from sqlalchemy import Integer,String,Column,ForeignKey, DateTime

class Post(Base):
    __tablename__ = "post_tbl"

    id = Column(Integer , primary_key=True)
    text = Column(String(30))
    date_time=Column(DateTime)
    profile_id = Column(Integer, ForeignKey("profile_tbl.id"))
    profle = relationship("Profile")

    def __init__(self, text,profile):
        self.text = text
        self.profle = profile
        #self.image=image
        self.date_time =datetime.now()

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())
