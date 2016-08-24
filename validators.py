import re

# from django
EMAIL_RE = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'  # quoted-string
    r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain

CN_MOBILE_RE = re.compile(
    r"(^(13\d|14[57]|15[^4\D]|17[13678]|18\d)\d{8}|170[^346\D]\d{7})$", re.IGNORECASE)


def is_email(s):
    """
    判断是否是邮箱地址格式
    :param s:
    :return: bool
    """
    return EMAIL_RE.match(s) is not None


def is_mobile(s):
    """
    判断指定字符串是否是手机号码格式
    :param s:
    :return:
    """
    return CN_MOBILE_RE.match(s) is not None


if __name__ == '__main__':
    test_emails = [
        'hello.world@gmail.com',
        '3.4@gmail.com.cn',
        'g3.4@gmail.ubfi',
        '#!world.g@gmMl.cddom.cn',
    ]

    for tm in test_emails:
        print(tm, is_email(tm))

    test_mobiles = [
        '13000010002',
        '1300001000',
        '19900010001',
        '13899999999',
        'fafsaga',
        '15000010000',
        '16000010000',
    ]

    for tm in test_mobiles:
        print(tm, is_mobile(tm))
