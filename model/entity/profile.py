from model.entity.base import Base
from sqlalchemy import Integer,String,Column,Boolean,Date,Time

class Profile(Base):
    __tablename__ = "profile_tbl"

    id = Column(Integer,primary_key=True)
    name=Column(String(30))
    family=Column(String(30))

    def __init__(self,id,name,family):
        self.id = id
        self.name = name
        self.family = family
        #self.username = username
        #self.password = password
        #self.email = email
        #self.image = image
        #self.status = status

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())