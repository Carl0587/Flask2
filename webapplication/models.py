from webapplication import db, loginManager
from datetime import datetime
from flask_login import UserMixin

@loginManager.user_loader
def loadUSer(userId):
    return  User.query.get(int(userId))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(210), unique=True, nullable=False)
    imageFile = db.Column(db.String(20), nullable=False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref= 'author', lazy= True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.imageFile}')"

#We are nor creating our post class to hold the posts from usernames
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    datePosted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.datePosted}')"

db.create_all()
#kkadfa