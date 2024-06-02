from model.da.database import DatabaseManager
from model.da.post_da import PostDa
from model.entity.post import Post
from model.entity.profile import Profile
from sqlalchemy import  or_,and_,between

#da=PostDa()

#da=DatabaseManager()

#pro=Profile("rezabgg","reztyhjyai")
#pro.status=1

#post=Post("hii",pro)
#da.save(post)

#post=Post("slm b hame",pro)
#da.save(post)

#for a in da.find_by_text("hame"):
 #   print(a.text)
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

pro=Profile("new1", "newer2")
#pro.status=False
pro=da.find_by_id(Profile,4)

post= Post("u?",pro)
da.save(post)

