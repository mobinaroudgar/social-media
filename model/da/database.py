from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database , database_exists

from model.entity.base import Base


class DatabaseManager:
    def make_engine(self):
        #Create Database
        if not database_exists("mysql+pymysql://root:root123@localhost:3306/social_media"):
            create_database("mysql+pymysql://root:root123@localhost:3306/social_media")
        self.engine=create_engine("mysql+pymysql://root:root123@localhost:3306/social_media")

        #Create Tables
        Base.metadata.create_all(self.engine)

        #Create Session(it does the same thing as a cursor)
        Session=sessionmaker(bind=self.engine)
        self.session=Session()


    def save(self,entity):
        self.make_engine()
        self.session.add(entity)
        self.session.commit()
        self.session.close()

    def edit(self,entity):
        self.make_engine()
        self.session.merge(entity)
        self.session.commit()
        self.session.close()

    def remove(self,entity):
        self.make_engine()
        entity=self.session.delete(entity)
        self.session.commit()
        self.session.close()
        return entity

    def find_all(self,class_name):
        self.make_engine()
        entity_list=self.session.query(class_name).all()
        self.session.close()
        return entity_list

    def find_by_id(self,class_name,id):
        self.make_engine()
        entity=self.session.get(class_name,id)
        self.session.close()
        return entity






















