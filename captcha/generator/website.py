from captcha.generator import Generator
from util.randstr import gen_website_captcha

DEFAULT_WEBSITE_CAPTCHA_LENGTH = 4


class WebsiteCaptchaGenerator(Generator):
    def generate_captcha_code(self):
        """
        网站端验证码是: 数字 + 大写字母，但是排除 0, 1, I, L, O 等不易识别的字符

        :param length: 长度
        :return: 全数字字符串
        """
        return gen_website_captcha(DEFAULT_WEBSITE_CAPTCHA_LENGTH)


if __name__ == '__main__':
    for _ in range(100):
        print(WebsiteCaptchaGenerator().generate_captcha_code(), end='\t')
