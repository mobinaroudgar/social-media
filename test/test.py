from model.da.database import DatabaseManager
from model.da.post_da import PostDa
from model.entity.post import Post
from model.entity.profile import Profile
from sqlalchemy import  or_,and_,between

#da=DatabaseManager()
#pro=Profile(3,"reza","rezai")
#da.save(pro)

#post=Post(2,"alyek",pro)
#da.save(post)

#post_list=da.find_all(Post)
#for post in post_list:
#    print(post.text,post.profile_id)

#search:
#da.make_engine()
#post_list=da.session.query(Post).filter(Post.text.like("%a%"))

#post_list=da.session.query(Post).filter(Post.profile_id==1)

#post_list=da.session.query(Post).filter(or_(Post.id>1,Post.text.like("a%")))

#post_list=da.session.query(Post).filter(between(Post.id,1,3))

#for post in post_list:
#    print(post.text,post.profile_id)



da=PostDa()
for a in da.find_by_text("a"):
    print(a.text)