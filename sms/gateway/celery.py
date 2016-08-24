from sms import Gateway


class CeleryGateway(Gateway):
    def send(self, mobile, message):
        pass