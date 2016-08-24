from app import db


class UserLogin(db.Model):
    __tablename__ = 'user_login'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True)
    last_ip = db.Column(db.String(16))
    last_login_time = db.Column(db.DateTime)