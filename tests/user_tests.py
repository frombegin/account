from unittest import TestCase
from unittest.mock import Mock, patch


def test_method():
    import os
    for x in os.walk('.'):
        print(x)


class UserTestCase(TestCase):
    def test_register(self):
        pass

    @patch('os.walk', return_value=['one', 'two', 'three'])
    def test_login_logout(self, walk):
        test_method()

    def test_find_password(self):
        mailsender = Mock(spec=['send', ])
        mailsender.send.return_value = True
        mailsender.send("tom@gmail.com", 3.14)
        mailsender.send.assert_called_with("tom@gmail.com", 3.14)
        self.assertTrue(mailsender.send("tom@gmail.com", 3.14))
