from account.services import (
    default_user_manager,
    user_resend_activation_email, RegistrationNotAllowedError)
from account.services.user_registration import AlreadyExistsError, UserRegistration
from account.signals import before_user_register, after_user_register
from app import app


def is_open_registration(app):
    return app.config.get('OPEN_REGISTRATION', True)


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
    invite_user = default_user_manager.get_user_by_token(token)

    # 处理非开放注册
    if not is_open_registration(app) and invite_user is None:
        raise RegistrationNotAllowedError('can''t register!')

    try:
        # 添加用户到数据库
        user = default_user_manager.add_user_to_db(email, password, invite_user)
        # 发送注册成功（激活）邮件
        user_resend_activation_email(email)
        # 发送“成功注册”事件
        after_user_register.send(email=email, invite_user=invite_user)
    except AlreadyExistsError as e:
        # 处理已经注册的情况
        pass


