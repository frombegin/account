from mail.sender import Sender


class Mailer:
    """
    flask extension
    """

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """

        :param app:
        :return:
        """
        # 获取配置

    def send(self, mail):
        pass
