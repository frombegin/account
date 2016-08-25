from account import before_user_register, after_user_register


class RegistrationNotAllowedError(RuntimeError):
    pass


class AlreadyExistsError(RuntimeError):
    pass


ERROR_USER_CATEGORY_BASE = 1000
ERROR_USER_ALREADY_EXISTS = ERROR_USER_CATEGORY_BASE + 1
ERROR_NOT_ALLOW_REGISTER = ERROR_USER_CATEGORY_BASE + 2
ERROR_NOT_ALLOW_REGISTER_WITHOUT_INVITER = ERROR_USER_CATEGORY_BASE + 3


class UserRegistrationError(RuntimeError):
    def __init__(self, code, message):
        super(UserRegistrationError, self).__init__()
        self.code = code
        self.message = message


class NotAllowRegisterError(UserRegistrationError):
    def __init__(self):
        self.code = ERROR_NOT_ALLOW_REGISTER
        self.message = ""


class UserRegistration:
    def __init__(self, email, password, token=None):
        self.email = email
        self.password = password
        self.token = token
        self.inviter = self.load_inviter(token)

    def load_inviter(self, token):
        if token is None:
            return None
            # TODO: load uer by token

    def _allow_open_register(self):
        return True

    def _allow_inviter_register(self):
        return True

    def check_allow(self):
        if self._allow_open_register():
            raise NotAllowRegisterError()

        if self._allow_inviter_register() and self.inviter is None:
            raise RegistrationNotAllowedError('can''t register without inviter!')

    def create_user(self):
        pass

    def send_activation_email(self):
        """
        发送注册成功（激活）邮件
        :return:
        """

    def execute(self):
        # 发送“开始注册”事件
        before_user_register.send(email=self.email, token=self.inviter)

        # 处理非开放注册
        self.check_allow()
        try:
            # 添加用户到数据库
            user = self.create_user()
            # 发送注册成功（激活）邮件
            self.send_activation_email()
            # 发送“成功注册”事件
            after_user_register.send(email=self.email, invite_user=self.inviter)

            return user
        except AlreadyExistsError as e:
            # 处理已经注册的情况
            pass


    def __call__(self, *args, **kwargs):
        return self.execute()


if __name__ == '__main__':
    UserRegistration('tom@email.com', '123456', '1234').execute()
    UserRegistration('tom@email.com', '123456', '1234')();