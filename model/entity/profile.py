class Profile:
    def __init__(self,id,name,family,username,password,email,image,status):
        pass

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())