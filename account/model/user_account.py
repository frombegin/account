from enum import Enum
from account.model import User
from app import db


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
    # 经过验证
    validated = db.Column(db.Boolean, default=False)

    # 索引
    __table_args__ = (
        db.Index('idx-account', "type", "account", unique=True),
    )
