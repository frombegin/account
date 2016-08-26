import string
import random
import functools

rand_string = lambda length, chars=string.ascii_uppercase + string.digits: ''.join(
    random.choice(chars) for _ in range(length)
)

# 移动端验证码全是: 数字
gen_mobile_captcha = functools.partial(rand_string, chars=string.digits)

# 网站端验证码是: 数字 + 大写字母，但是排除 0, 1, I, L, O 等不易识别的字符
gen_website_captcha = functools.partial(rand_string, chars='23456789ABCDEFGHJKMNPQRSTUVWXYZ')

# 产生找回密码的hash
gen_password_reset_hash = functools.partial(rand_string, chars='23456789ABCDEFGHJKMNPQRSTUVWXYZ')

if __name__ == '__main__':
    print([gen_website_captcha(8) for _ in range(15)])
    print([gen_mobile_captcha(4) for _ in range(15)])
