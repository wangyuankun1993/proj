import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    """
    GET请求
    """
    def get(self):
        self.render('login.html')

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is login page")

    def post(self):
        username = self.get_argument('username','') # 接收用户名参数
        password = self.get_argument('password','') # 接收密码参数
        self.write("username is {}, password is {}".format(username,password))

def make_app():
    """
    创建Tornado应用
    """
    return tornado.web.Application(
        handlers = [
            (r"/", MainHandler), # 设置路由
            (r"/login", LoginHandler), # 设置登录页路由
            ],
        debug = True, # 开启调试模式
        static_path = os.path.join(os.path.dirname(__file__),'static'), # 设置静态资源路径
        template_path = os.path.join(os.path.dirname(__file__),"templates"), # 设置模板路径
    )

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    print('Starting server on port 8888...')
    tornado.ioloop.IOLoop.current().start()
