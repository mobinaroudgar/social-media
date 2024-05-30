from model.da.database import DatabaseManager
from model.entity.post import Post
from model.entity.profile import Profile

da=DatabaseManager()
pro=Profile(4,"ali","alipour")
da.save(pro)

post=Post(4,"salam")
da.save(post)