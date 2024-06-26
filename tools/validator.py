import re


class validator:
    @classmethod
    def is_persion(cls,text,length=10,message="invalid"):
        if  not re.match("^[\sآ-ی]{2,"+str(length) + "}$",text):
            raise ValueError(message)


    @classmethod
    def is_english(cls,text,length=10,message="invalid"):
        if not re.match("^[\sa-zA-Z]{2,"+str(length) + "}$",text):
            raise ValueError(message)



    @classmethod
    def is_number(cls,number , is_positive=False,message="Invalid"):
        if is_positive:
            if not number>0:
                raise ValueError(message)

        if not (isinstance(number,int) or isinstance(number,float)):
            raise ValueError(message)