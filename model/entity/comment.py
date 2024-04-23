class Comment:
    def __init__(self,id,post,profile,text,date_title):
        pass

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())