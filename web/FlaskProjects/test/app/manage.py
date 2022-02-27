from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_migrate import Migrate
from flask_script import Manager, Shell, Server

app = Flask(__name__)
app.debug = True

# 基本配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://root:wangyuankun1993@localhost/flask_demo'
        )

# 实例化SQLAlchemy类
db = SQLAlchemy(app)

# 创建Migrate实例
migrate = Migrate(app,db)

# 实例化Manager类
manager = Manager(app)

# 新增db命令
manager.add_command("runserver",Server())

@app.route('/')
def hello():
    return "Hello World!"

# 设置ORM类
class User(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
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
