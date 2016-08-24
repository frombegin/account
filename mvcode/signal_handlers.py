from app import app
from mvcode import mvcode_generated, mvcode_verified


@mvcode_generated.connect_via(app)
def log_mvcode_generated(sender, mobile, used_for, mvcode):
    print('创建手机验证码', mobile, used_for, mvcode)


@mvcode_verified.connect_via(app)
def log_mvcode_verified(sender, mobile, used_for, mvcode, result):
    print('检验手机验证码', mobile, used_for, mvcode, result)