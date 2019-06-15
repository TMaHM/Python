"""
能防断网，但是防不了状态错乱
"""

from phones import *
from dutconfigs import *


def check_multi_paging(dut_A, dut_B):
    lineKeyType = dut_A.get_line_key('l14')['type']
    if lineKeyType.lower() is not 'multicast paging':
        dut_A.set_line_key(testKey, testFunction, multicastAddress, label=label)

    url = '%sP20021=%s' % (dut_B.url.setting, multicastAddress)
    requests.get(url)


def multicast_paing(dut_A, dut_B):
    import time

    sPaging = dut_A.press_key(testKey)
    if sPaging:
        log.info("Start Multicast Paging OK.")
    else:
        log.info("Start Multicast Paging Failed, Retry Now.")
        multicast_paing(dut_A, dut_B)
    time.sleep(3)

    ePaging = dut_A.press_key('f4')
    if ePaging:
        log.info("End Multicast Paging OK.")
    else:
        log.info("End Multicast Paging Failed, Retry Now.")
        multicast_paing(dut_A, dut_B)

    print("Multicast Paging %d times." % i)

    time.sleep(2)

# 实例化dut_A, dut_B
phoneA = Phone('10.3.2.47')
phoneB = Phone('10.3.2.229')

# 检查状态后开始测试循环
check_multi_paging(phoneA, phoneB)
for i in range(10000):
    multicast_paing(phoneA, phoneB)
