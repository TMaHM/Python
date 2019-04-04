from status import *
from phones import *

import requests
import time

cnt = 0

# pR is DUT
# The scenario: pA calls pR, pR answer the call, then blind transfer the call by expansion to pB.
# So the pR must set dsskey transfer mode as Blind Transfer.
# And pR need be confirmed its extension number, so pA can call it.
pA = Phone('10.3.2.180')
# pB = Phone('192.168.1.70')
# pR = Phone('192.168.1.65', extension='047')


pA.set_key('l2', 'blf', '2052')