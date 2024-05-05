from model.entity.base import Base


class Profile(Base):
    __tablename__ = "profile_tbl"
    def __init__(self,id,name,family,username,password,email,status):
        self.id = id
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.email = email
        #self.image = image
        self.status = status

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())