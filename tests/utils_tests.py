from unittest import TestCase
from validators import is_mobile, is_email

class UtilsTestCase(TestCase):

    def test_email_validator(self):
        self.assertTrue(is_email("hello.world@gmail.com"))
        self.assertFalse(is_email("hello.world @ gmail.com"))
        self.assertTrue(is_email("g3.4@gmail.ubfi"))
        self.assertTrue(is_email("#!world.g@gmMl.cddom.cn"))

    def test_mobile_validator(self):
        self.assertTrue(is_mobile('13000010002'))
        self.assertFalse(is_mobile('1300001000'))
        self.assertFalse(is_mobile('19900010001'))
        self.assertTrue(is_mobile('13899999999'))
        self.assertFalse(is_mobile('fafsaga'))
        self.assertTrue(is_mobile('15000010000'))
        self.assertFalse(is_mobile('16000010000'))