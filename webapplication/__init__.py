from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)

app.config['SECRET_KEY']= 'eb69c8bfa9ed26d632149db8322b3682'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///.appDatabase.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
loginManager.login_view= 'login'
loginManager.login_message_category= 'info'


from webapplication import routes

