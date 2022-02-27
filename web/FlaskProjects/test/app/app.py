from flask_script import Manager
from flask import Flask

app = Flask(__name__)
# 配置app
app.debug = True
manager = Manager(app)

@manager.option("-n","--name",help="Your name")
def hello(name):
    print("hello {}".format(name))

if __name__ == '__main__':
    manager.run()
