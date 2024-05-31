from model.da.database import DatabaseManager
from model.entity.post import Post


class PostDa(DatabaseManager):
    def find_by_text(self,word):
        self.make_engine()
        post_list=self.session.query(Post).filter(Post.text.like(f"%{word}%"))
        self.session.close()
        return post_list