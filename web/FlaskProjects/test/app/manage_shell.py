from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_migrate import Migrate
from flask_script import Manager, Shell

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://root:wangyuankun1993@localhost/flask_demo'
        )

db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)

def make_shell_context():
    return dict(app=app,db=db,User=User,Article=Article)

manager.add_command("shell",Shell(make_context=make_shell_context))

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    articles = db.relationship('Article')
    gender = db.Column(db.BOOLEAN,default=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),index=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Article %r>' % self.title

if __name__ == '__main__':
    manager.run()
