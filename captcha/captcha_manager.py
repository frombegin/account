from enum import Enum


class CaptchaUsage(Enum):
    REGISTRATION = 'registration'


class CaptchaManager:
    def generate(self, used_for):
        """
        :return:
        """

    def verify(self, captcha, used_for, remove_on_verified=True):
        pass
