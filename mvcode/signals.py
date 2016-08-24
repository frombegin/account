from blinker import Namespace

my_signals = Namespace()

mvcode_generated = my_signals.signal('mvcode.generated')
mvcode_verified = my_signals.signal('mvcode.verified')