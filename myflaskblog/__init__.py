
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f18ba0230f5f7ccc16ca6ffa92f75997'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from myflaskblog import routes