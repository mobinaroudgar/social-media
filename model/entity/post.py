class Post:
    def __init__(selfcode,id,profile,text,image,date_time):
        pass

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return  tuple(self.__dict__.values())
