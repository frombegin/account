from account.model import User
from app import db
from sqlalchemy import func
from util.randstr import gen_password_reset_hash
from datetime import datetime, timedelta
from flask import current_app

DEFAULT_RESET_PASSWORD_EXPIRATION_DURATION = 4 * 3600  # 4 小时


class ResetPassword(db.Model):
    __tablename__ = 'reset_password'
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户 id
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    # 邮件激活代码
    reset_hash = db.Column(db.String, index=True)
    # 邮件激活过期时间
    reset_expired_time = db.Column(db.DateTime)


class ResetPasswordManager:
    def request_reset_password(self, email):
        # 判断用户是否存在
        user = db.session.query(User.id).filter(User.email == email).one_or_none()
        if user:
            # 产生一个 reset_hash
            reset_hash = gen_password_reset_hash(8)

            # 将 reset_hash 写入数据库中
            rp = ResetPassword(
                user_id=user.id,
                reset_hash=reset_hash,
                reset_expired_time=datetime.now() + timedelta(seconds=self.get_expiration_duration())
            )
            db.session.add(rp)
            db.session.commit()

            # 发送 reset_hash 邮件
            self.send_reset_password_email(email, reset_hash)
            return True
        return False

    def get_expiration_duration(self):
        return current_app.config.get('RESET_PASSWORD_EXPIRATION_DURATION', DEFAULT_RESET_PASSWORD_EXPIRATION_DURATION)

    def handle_reset_password(self, email, reset_hash, new_password):
        # 查询满足条件的用户
        user = db.session.query(User).join(ResetPassword, User.id == ResetPassword.user_id).filter(
            User.email == email,
            ResetPassword.reset_hash == reset_hash,
            ResetPassword.reset_expired_time <= func.now()).one_or_none()

        if user:
            # 存在此用户，则修改密码
            user.password_hash = new_password
            db.session.add(user)
            db.session.commit()  # rollback..
            return True
        return False

    def send_reset_password_email(self, email, reset_hash):
        """
        发送 reset_hash 邮件

        :param email: 目标邮箱
        :param reset_hash: reset_hash 字符串
        :return:
        """


if __name__ == '__main__':
    from app import app

    with app.app_context():
        rpm = ResetPasswordManager()
        print(rpm.get_expiration_duration())
        rpm.request_reset_password('tom@gmail.com')
        rpm.handle_reset_password('tom@gmail.com', '12435', 'newpass')
