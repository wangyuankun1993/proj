from flask import Flask, url_for, redirect, render_template, request, make_response, session
#from app.home import home as home_blueprint
#from app.admin import admin as admin_blueprint
app = Flask(__name__)
app.secret_key = 'wangyuankun1993'

# 注册蓝图
#app.register_blueprint(home_blueprint, url_prefix='/home')
#app.register_blueprint(admin_blueprint, url_prefix='/admin')

# 实现一个可以求长度的函数
@app.template_filter
def count_length(arg):
    return len(arg)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/contact')
def about():
    return render_template('contact.html')

# 在第一次请求之前运行
@app.before_first_request
def before_first_request():
    print("before_first_request")

# 在每一次请求前都会执行
@app.before_request
def before_request():
    print("before_request")

# 在请求之后运行
@app.after_request
def after_request(response):
    print("after_request")
    return response

# 无论视图函数是否出现异常，每一次请求之后都会调用，会接受一个参数，参数是服务器出现的错误信息
@app.teardown_request
def teardown_request(error):
    print("teardown_request: error %s" % error)

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示该用户名的用户信息
    return f'用户名是:{username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 根据ID显示文章，ID是整型数据
    return f'ID是:{post_id}'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'wangyuankun' and password == 'wangyuankun1993':
            # 如果用户名和密码正确，将用户名写入session
            session['username'] = username
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/upload',methods=['GET','POST'])
def upload():
    """
    头像上传表单页面
    """
    if request.method == 'POST':
        # 接收头像字段
        avatar = request.files['avatar']
        # 判断文件是否上传，已经上传的文件类型是否正确
        if avatar and allowed_file(avatar.filename):
            # 生成随机文件名
            filename = random_file(avatar.filename)
            # 保存文件
            avatar.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('uploaded_file',filename=filename))
    return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

def random_file(filename):
    # 获取文件后缀
    ext = os.path.splitext(filename)[1]
    # 使用uuid生成随机字符
    new_filename = uuid.uuid4().hex+ext
    return new_filename

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
