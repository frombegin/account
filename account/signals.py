from blinker import Namespace

my_signals = Namespace()

before_user_login = my_signals.signal('before-user-login')
after_user_login = my_signals.signal('after-user-login')
before_user_register = my_signals.signal('before_user_register')
after_user_register = my_signals.signal('after_user_register')
