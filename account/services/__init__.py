from account import before_user_register, before_user_login
from account.services.user_register_email import is_open_registration, NotOpenRegistrationError, AlreadyExistsError
from account.user_manager import default_user_manager
from app import app


# def user_register(account, password, token):
#     if validators.is_mobile(account):
#         return user_register_mobile(account, password, token)
#     elif validators.is_email(account):
#         return user_register_email(account, password, token)
#     else:
#         raise BadFormatException("非法账户格式: {}".format(account))
# class BadFormatException(RuntimeError):
#     pass


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
    invite_user = default_user_manager.get_user_by_token(token)

    # 处理非开放注册
    if not is_open_registration(app) and invite_user is None:
        raise NotOpenRegistrationError('can''t register!')

    try:
        # 添加用户到数据库
        user = default_user_manager.add_user_to_db(mobile, password, invite_user)
    except AlreadyExistsError as e:
        # 处理已经注册的情况
        pass


        # 发送手机验证码
        # 发送“成功注册”事件


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
