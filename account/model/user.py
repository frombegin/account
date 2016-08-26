from enum import Enum

from sqlalchemy import func

from app import db


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



