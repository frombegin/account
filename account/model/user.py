from sqlalchemy import func

from app import db
from enum import Enum


class User(db.Model):
    __tablename__ = 'user'
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户昵称
    nickname = db.Column(db.String(80), nullable=False)
    # 邮箱
    email = db.Column(db.String(128), nullable=False)
    # 邮件是否激活
    email_activated = db.Column(db.Boolean, default=False)
    # 创建时间
    created_at = db.Column(db.DateTime, server_default=func.now())
    # 更新时间
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    # 密码 hash
    password_hash = db.Column(db.String(128), nullable=False)
    # 当前是否可用
    enabled = db.Column(db.Boolean, default=True)

    @staticmethod
    def auth(email, password):
        pass


# def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
# ...    return ''.join(random.choice(chars) for _ in range(size))

import string
import random

rand_str = lambda size=6, chars=string.ascii_uppercase + string.digits: ''.join(
    random.choice(chars) for _ in range(size)
)


class CaptchaUsage(Enum):
    REGISTRATION = 'registration'


class CaptchaManager:
    def generate(self, used_for):
        """
        :return:
        """
        import random
        random.randrange()

    def verify(self, code, used_for, remove_after_verfied=True):
        pass


class PasswordResetManager:
    pass


class EmailActivationManager:
    pass


class UserResetPassword(db.Model):
    __tablename__ = 'user_reset_password'
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户 id
    user_id = db.Column(db.Integer, db.foreign(User.id))
    # 邮件激活代码
    reset_hash = db.Column(db.String, index=True)
    # 邮件激活过期时间
    reset_expired_time = db.Column(db.DateTime)


class UserActivation(db.Model):
    __tablename__ = 'user_activation'
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户 id
    user_id = db.Column(db.Integer, db.foreign(User.id))
    # 邮件激活代码
    activation_code = db.Column(db.String, index=True)
    # 邮件激活过期时间
    activation_expired_time = db.Column(db.DateTime)


class AccountType(Enum):
    EMAIL = 'email'
    MOBILE = 'mobile'
    QQ = 'qq'


class UserAccount(db.Model):
    __tablename__ = 'user_account'
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户 id
    user_id = db.Column(db.Integer, db.foreign(User.id))
    # 账户类型
    type = db.Column(db.String(16), nullable=False)
    # 账户 id
    account = db.Column(db.String(255), nullable=False)
    # 索引
    __table_args__ = (
        db.Index('idx-account', "type", "account", unique=True),
    )
