# 导入ioloop模块
import tornado.ioloop

# 导入web模块
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    """
    GET请求
    """
    def get(self):
        self.write("Hello World!")

def make_app():
    """
    创建Tornado应用
    """
    return tornado.web.Application([
        (r"/", MainHandler), # 设置路由
    ])

if __name__ == '__main__':
    app = make_app() # 创建Tornado应用
    app.listen(8888) # 设置监听端口
    print('Starting server on port 8888...')
    tornado.ioloop.IOLoop.current().start() # 启动服务
