from account.model import User
from app import db


class MailActivation(db.Model):
    __tablename__ = 'mail_activation'
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户 id
    user_id = db.Column(db.Integer, db.foreign(User.id))
    # 邮件激活代码
    activation_code = db.Column(db.String, index=True)
    # 邮件激活过期时间
    activation_expired_time = db.Column(db.DateTime)


class MailActivationManager:
    pass
