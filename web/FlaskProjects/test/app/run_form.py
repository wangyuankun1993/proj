from flask import Flask, url_for, redirect, render_template
from models import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wangyuankun1993'

@app.route('/login',method=['GET','POST'])
def login():
    """
    登陆页面
    """
    form = LoginForm()
    if form.validate_on_submit():
        username = form.name.data
        password = form.password.data
        if username == 'wangyuankun' and password == 'wangyuankun1993':
            return redirect(url_for('index'))
    return render_template('login.html',form=form)

@app.route('/')
def index():
    """
    首页
    """
    name = "雨琨教育集团"
    message = """
        雨琨教育集团成立于2022年1月1日，是一家集小、初、高、大学教育为一体的培训机构
    """
    return render_template('index.html',name=name,message=message)

if __name__ == '__main__':
    app.run_form(debug=True)
