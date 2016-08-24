from signals import mvcode_generated, mvcode_verified


class SMSGateway:
    def send(self, mobile, message):
        """

        :param mobile:
        :param message:
        :return:
        """


default_sms_gateway = SMSGateway()
default_sms_gateway.send("13000010002", "hello world")


class MvcodeGenerator:
    def generate(self, max_length=4):
        import random
        return str(random.randint(1000, 9999))


default_mvcode_generator = MvcodeGenerator()
DEFAULT_MVCODE_EXPIRATION_TIME = 30  # 30 seconds
MVCODE_SMS_TEMPLATE = 'your mvcode is {}'


class MvcodeStore:
    def store(self, mobile, used_for, mvcode):
        pass

    def verify(self, mobile, used_for, mvcode):
        """
        检验 mvcode
        :param mobile:
        :param used_for:
        :param mvcode:
        :return:
        """
        return True

    def _create_key(self, mobile, used_for):
        return "{}-{}".format(mobile, used_for)


default_mvcode_store = MvcodeStore()


class MvcodeService:
    def generate_mvcode(self, mobile, used_for='registration'):
        # 产生验证码
        mvcode = default_mvcode_generator.generate()
        # 发送短信验证码
        default_sms_gateway.send(mobile, MVCODE_SMS_TEMPLATE.format(mvcode))
        # 保存在临时存储中
        default_mvcode_store.store(mobile, used_for, mvcode)
        # 发送 产生手机验证码 事件
        mvcode_generated.send(app, mobile=mobile, used_for=used_for, mvcode=mvcode)

    def verify_mvcode(self, mobile, mvcode, used_for='registration'):
        # 校验指定的验证码是否正确
        result = default_mvcode_store.verify(mobile, used_for, mvcode)
        # 发送 验证手机验证码 事件
        mvcode_verified.send(app, mobile=mobile, used_for=used_for, mvcode=mvcode, result=result)
        return result


mvcode_service = MvcodeService()


from account import app

@mvcode_generated.connect_via(app)
def log_mvcode_generated(sender, mobile, used_for, mvcode):
    print('创建手机验证码', mobile, used_for, mvcode)


@mvcode_verified.connect_via(app)
def log_mvcode_verified(sender, mobile, used_for, mvcode, result):
    print('检验手机验证码', mobile, used_for, mvcode, result)
