from website import db
from website.models import User, Post

# users = User.query.all()

# for user in users:
#     print(user)


posts = Post.query.all()

for post in posts:
    print(post.text)