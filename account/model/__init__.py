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
