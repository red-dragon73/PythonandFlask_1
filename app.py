from flask import Flask
from flask_sqlalchemy import SQLAlchemy

my_app = Flask(__name__)
my_app.config['SECRET_KEY'] = "Hello"
my_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(my_app)

from routes import *

if __name__ == "__main__":
    my_app.run(debug=True)
