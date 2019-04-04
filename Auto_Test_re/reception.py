from status import *
from phones import *

import requests
import time

cnt = 0

# pR is DUT
# The scenario: pA calls pR, pR answer the call, then blind transfer the call by expansion to pB.
# So the pR must set dsskey transfer mode as Blind Transfer.
# And pR need be confirmed its extension number, so pA can call it.
pA = Phone('192.168.1.64')
pB = Phone('192.168.1.70')
pR = Phone('192.168.1.65', extension='047')

while True:

    pA.dial(pR.ext)
    time.sleep(3)

    pR.answer('SPEAKER')
    time.sleep(2)

    pR.exp_blf('l2')
    time.sleep(2)

    pB.answer('speaker')
    time.sleep(2)

    pA.end_call('SPEAKER')
    time.sleep(1)

    cnt += 1
    print(cnt)
