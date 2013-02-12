from flask import Flask

from flaskext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float
import config

#db class
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db = SQLAlchemy(app)

#db classes
class PageContent(db.Model):
    __tablename__ = 'page_content'

    def __init__(self):
        return

    def __repr__(self):
        return 'Yah mama so fat'


