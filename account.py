from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

import validators
from mvcode import mvcode_service
from signals import before_user_login, before_user_register, after_user_register

app = Flask(__name__)

app.config.update({
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_ECHO': True,
})

account_config = {
    'OPEN_REGISTRATION': False,
}

app.config.update(account_config)

########################################################################################################################

db = SQLAlchemy()
db.init_app(app)



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


########################################################################################################################

class User(db.Model):
    __tablename__ = 'user'

    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户昵称
    nickname = db.Column(db.String(80), nullable=False)
    # 邮箱
    email = db.Column(db.String(128), nullable=False)
    # 密码 hash
    password_hash = db.Column(db.String(128), nullable=False)
    # 创建时间
    created_at = db.Column(db.DateTime, server_default=func.now())
    # 更新时间
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    # 邮件激活代码
    activation_code = db.Column(db.String)
    # 邮件是否激活
    email_activated = db.Column(db.Boolean, default=False)
    # 重置密码 token 的 hash
    reset_hash = db.Column(db.String(128))
    # 发送重置邮件的时间
    reset_time = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def auth(email, password):
        pass


class UserLogin(db.Model):
    __tablename__ = 'user_login'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True)
    last_ip = db.Column(db.String(16))
    last_login_time = db.Column(db.DateTime)


########################################################################################################################


class BadFormatException(RuntimeError):
    pass


def user_register(account, password, token):
    if validators.is_mobile(account):
        return user_register_mobile(account, password, token)
    elif validators.is_email(account):
        return user_register_email(account, password, token)
    else:
        raise BadFormatException("非法账户格式: {}".format(account))


def get_user_by_token(token):
    """
    根据 token 获取邀请人, token 不存在时返回 None

    :param token:
    :return: User
    """


def is_open_registration(app):
    return app.config.get('OPEN_REGISTRATION', True)


class NotOpenRegistrationError(RuntimeError):
    pass


def register_user(mobile, password, invite_user):
    pass


class AlreadyExistsError(RuntimeError):
    pass


def user_register_mobile(app, mobile, password, token=None):
    """

    :param mobile:
    :param password:
    :param token:
    :return:
    """
    # 发送“开始注册”事件
    before_user_register.send(mobile=mobile, token=token)

    # 根据 token 获取邀请人
    invite_user = get_user_by_token(token)

    # 处理非开放注册
    if not is_open_registration(app) and invite_user is None:
        raise NotOpenRegistrationError('can''t register!')

    try:
        # 添加用户到数据库
        user = register_user(mobile, password, invite_user)
    except AlreadyExistsError as e:
        # 处理已经注册的情况
        pass


        # 发送手机验证码
        # 发送“成功注册”事件


def user_register_email(email, password, token):
    """
    注册新用户
    :param email:
    :param password:
    :param token:
    :return:
    """

    # 发送“开始注册”事件
    before_user_register.send(email=email, token=token)

    # 根据 token 获取邀请人, token 不存在时返回 None
    invite_user = get_user_by_token(token)

    # 处理非开放注册
    if not is_open_registration(app) and invite_user is None:
        raise NotOpenRegistrationError('can''t register!')

    try:
        # 添加用户到数据库
        user = register_user(email, password, invite_user)
        # 发送注册成功（激活）邮件
        user_resend_activation_email(email)
        # 发送“成功注册”事件
        after_user_register.send(email=email, invite_user=invite_user)
    except AlreadyExistsError as e:
        # 处理已经注册的情况
        pass


def user_resend_activation_email(email):
    """
    重新发送激活邮件
    :param email:
    :return:
    """


def user_activate_email(email, activation_code):
    """
    激活邮件
    :param email:
    :param activation_code:
    :return:
    """


def user_send_reset_password_email(email):
    """
    发送找回密码邮件
    :param email:
    :return:
    """


def user_reset_password(email, reset_token, new_password):
    """
    通过找回密码token, 重置密码
    :param email:
    :param reset_token:
    :param new_password:
    :return:
    """


def user_login(email, password):
    """
    用户登录
    :param email:
    :param password:
    :return:
    """
    app.logger.info(email)
    before_user_login.send(email)


def user_logout(session_id):
    """
    用户注销
    :param session_id:
    :return:
    """


def user_get_profile(session_id):
    """
    获取用户资料
    :param session_id:
    :return:
    """


def user_set_profile(session_id, profile):
    """
    设置用户资料
    :param session_id:
    :param profile:
    :return:
    """


########################################################################################################################

@app.route('/')
def hello_world():
    # user_login("hello@email.com", '123456')
    mvcode_service.generate_mvcode('13000010002')

    mvcode_service.verify_mvcode('13000010002', '3214', 'message')
    # before_user_login.send(app, email="hello@email.com")
    #
    # print(request.remote_addr)
    # print(request.access_route)
    #
    # # print(request.remote_addr)
    # print(request.remote_user)
    # for h in request.headers:
    #     print(h)

    return 'Hello World!' + str(is_open_registration(current_app))


if __name__ == '__main__':
    app.run(debug=True)
