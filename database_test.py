from app import db
from website.models import User

users = User.query.all()

for user in users:
    print(user)