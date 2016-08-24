from sms.gateway.null import NullGateway
from sms.gateway.celery import CeleryGateway

class Gateway:
    def send(self, mobile, message):
        """

        :param mobile:
        :param message:
        :return:
        """


