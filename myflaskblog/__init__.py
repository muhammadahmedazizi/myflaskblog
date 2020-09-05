import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from myflaskblog.secret import email, ps





app = Flask(__name__)
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f18ba0230f5f7ccc16ca6ffa92f75997'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#EMAIL SETTING FOR GMAIL
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['DEBUG'] = True
app.config['MAIL_USERNAME'] = 'dummy@dummy.com'
app.config['MAIL_PASSWORD'] = 'dummypassword'
mail = Mail(app)


from myflaskblog import routes