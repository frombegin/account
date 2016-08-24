from account import before_user_login
from app import app


@before_user_login.connect_via(app)
def guess_password_checker(sender, email):
    """
    检测 用户是否正在试图猜测密码
    """
    print(sender, type(sender))
    print("用户是否正在试图猜测密码: {}".format(email))


@before_user_login.connect_via(app)
def crawler_checker(sender, email):
    """
    用户近期频繁登录 检测
    """


@before_user_login.connect_via(app)
def ip_checker(sender, email):
    """
    用户的IP更改 检测
    """


@before_user_login.connect_via(app)
def robot_activity_checker(sender, email):
    """
    用户短期内执行大量活动（自动化脚本） 检测
    """