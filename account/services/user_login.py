from account import before_user_login
from account.signals import after_user_login


class UserLogin:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def authenticate(self):
        pass

    def user_already_login(self):
        """
        用户已经登录
        :return:
        """

    def create_session(self):
        pass

    def execute(self):
        # 发送“开始登录”事件
        before_user_login.send(email=self.email, token=self.inviter)

        # 根据账户密码进行认证
        auth_info = self.authenticate()
        if auth_info:
            if self.user_already_login():
                pass  # kick off already logined user?

            session_id = self.create_session()
            after_user_login.send()  # 发送“成功登录”事件