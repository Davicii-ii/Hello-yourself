from seq2frames import use_win, use_lin

import sys

print('hello\n')

if sys.platform == 'win32':
    use_win()
else:
    use_lin()
