from app import app
from mvcode.signals import mvcode_generated, mvcode_verified
from sms.gateway import Gateway as SMSGateway
from mvcode.generator import Generator
from mvcode.store import Store
from mvcode.usage import Usage

MVCODE_SMS_TEMPLATE = 'your mvcode is {}'


class MvcodeService:
    def __init__(self, generator: Generator, sms_gateway: SMSGateway, store: Store,
                 length: int = 4, template: str = MVCODE_SMS_TEMPLATE):
        super(MvcodeService, self).__init__()
        self._generator = generator
        self._sms_gateway = sms_gateway
        self._store = store
        self._mvcode_length = length
        self._template = template

    def generate_mvcode(self, mobile, used_for=Usage.REGISTRATION):
        # 产生验证码
        mvcode = self._generator.generate_mvcode(self._mvcode_length)
        # 发送短信验证码
        self._sms_gateway.send(mobile, self._template.format(mvcode))
        # 保存在临时存储中
        self._store.save(mobile, used_for.name, mvcode)
        # 发送 产生手机验证码 事件
        mvcode_generated.send(app, mobile=mobile, used_for=used_for, mvcode=mvcode)

    def verify_mvcode(self, mobile, mvcode, used_for=Usage.REGISTRATION):
        # 校验指定的验证码是否正确
        result = self._store.verify(mobile, used_for.name, mvcode)
        # 发送 验证手机验证码 事件
        mvcode_verified.send(app, mobile=mobile, used_for=used_for, mvcode=mvcode, result=result)
        return result

        # mvcode_service = MvcodeService()
