"""
1.View history
    1.1 All Calls
    1.2 Missed Calls
    1.3 Received Calls
    1.4 Dialed Calls
    1.5 Forwarded Calls
2.Delete history
3.Option - Show Detail
    3.1 Dial from Detail
4.Option - Add to Contacts
5.Option - Add to Blacklist
6.Option - Delete All
"""

from phones import *

# Global Configuration
DUT_A = {'ip': '10.3.2.229', 'ext': '8724'}

# Initial DUT
phoneA = Phone(DUT_A['ip'])

def view_history(dut_A):

    dut_A.press_key('f1')
    time.sleep(1)
    dut_A.set_idle_status()


view_history(phoneA)