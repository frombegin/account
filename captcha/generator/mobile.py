from captcha.generator import Generator
from util.randstr import gen_mobile_captcha

DEFAULT_MOBILE_CAPTCHA_LENGTH = 4


class MobileCaptchaGenerator(Generator):
    def generate_captcha_code(self):
        """
        移动端验证码全是: 10进制 数字

        :param length: 长度
        :return: 全数字字符串
        """
        return gen_mobile_captcha(DEFAULT_MOBILE_CAPTCHA_LENGTH)


if __name__ == '__main__':
    print(MobileCaptchaGenerator().generate_captcha_code())
