from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    """
    登录表单类
    """
    name = StringField(label='用户名',validators=[
            DataRequired("用户名不能为空"),
            Length(max=10,min=3,message="用户名长度必须大于3且小于10")
        ])
    password = PasswordField(label='密码',validators[
            DataRequired("密码不能为空"),
            Length(max=10,min=6,message="用户名长度必须大于6且小于10")
        ])
    submit = SubmitField(label='提交')
