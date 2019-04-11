from phones import *
import time

"""
Attended Transfer
Semi-Attended Transfer
Blind Transfer
Accept the instantiation of class Phone() as parameters.
"""

def attended_Transfer(*phone):

    if len(phone) == 3:
        pA = phone[0]
        pB = phone[1]
        pC = phone[2]
        # A call B
        pA.dial(pB.ext)
        time.sleep(1)
        # B answer
        pB.answer('speaker')
        time.sleep(2)
        # B AT to C
        pB.transfer(pC.ext, 'AT')
        time.sleep(1)
        # C answer
        pC.answer('F1')
        time.sleep(2)
        # B press transfer
        pB.transfer()
        # A C in talking
        time.sleep(2)
        # C end call
        pC.end_call('X')
        log.info('Attended Transfer test [OK]...')

    else:
        error_info = 'Transfer scripts need 3 param, you input ' + str(len(phone))
        print(error_info)
        log.info(error_info)

def semi_Attended_Transfer(*phone):
    if len(phone) == 3:
        pA = phone[0]
        pB = phone[1]
        pC = phone[2]

        # A call B
        pA.dial(pB.ext)
        time.sleep(1)
        # B answer
        pB.answer('speaker')
        time.sleep(2)
        # B SAT to C
        pB.transfer(pC.ext, 'SAT')
        time.sleep(1)
        pB.transfer()
        # C answer
        pC.answer('speaker')
        # A C in talking
        time.sleep(2)
        # C end call
        pC.end_call('x')

    else:
        error_info = 'Transfer scripts need 3 param, you input ' + str(len(phone))
        print(error_info)
        log.info(error_info)


def blind_Transfer(*phone):
    if len(phone) == 3:
        pA = phone[0]
        pB = phone[1]
        pC = phone[2]

        # A call B
        pA.dial(pB.ext)
        time.sleep(1)
        # B answer
        pB.answer('speaker')
        time.sleep(1)
        # B BT to C
        pB.transfer(pC.ext, 'BT')
        time.sleep(1)
        # C answer the call
        pC.answer('speaker')
        # A C in talking
        time.sleep(2)
        pC.end_call('x')

    else:
        error_info = 'Transfer scripts need 3 param, you input ' + str(len(phone))
        print(error_info)
        log.info(error_info)