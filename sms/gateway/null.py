from sms import Gateway


class NullGateway(Gateway):
    def send(self, mobile, message):
        pass
