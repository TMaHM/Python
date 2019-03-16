from status import *
from phones import *

import requests
import time

cnt = 0
# ip_R = input('Enter IP of DUT - Reception: ')
# ip_A = input('Enter IP of Phone A: ')
# ip_B = input('Enter IP of Phone B: ')



# pA = Phone(ip_A)
# pB = Phone(ip_B)
# pR = Phone(ip_R, extension='8724')

pA = Phone('10.3.2.3')
pB = Phone('10.3.2.205')
pR = Phone('10.3.2.180', extension='8724')

while True:
    pA.dial(pR.ext, account='Account=6')
    time.sleep(3)

    pR.answer('SPEAKER')
    time.sleep(2)
    pR.set_key('l2', 'blf', '2051')

    pR.press_key('l2')
    # pR.exp_blf('l1')
    time.sleep(2)

    pB.answer('speaker')
    time.sleep(2)

    pA.end_call('SPEAKER')
    time.sleep(1)


    cnt += 1
    print(cnt)
