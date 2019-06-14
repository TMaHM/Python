"""
能防断网，但是防不了状态错乱
"""

from phones import *

phoneA = Phone('10.3.2.47')
phoneB = Phone('10.3.2.229')

testKey = 'l14'
testFunction = 'multicast paging'
multicastAddress = '224.10.20.20:2020'
label = 'AutoTestMPaging'

def multicastPaing(phoneA, phoneB):
    import time
    import requests
    # lineKeyType = phoneA.get_line_key('l14')
    # if lineKeyType.lower() is not 'multicast paging':  # 好像这里判断的意义不大
    phoneA.set_line_key(testKey, testFunction, multicastAddress, label=label)
    url = '%sP20021=%s' % (phoneB.url.setting, multicastAddress)
    requests.get(url)

    sPaging = phoneA.press_key(testKey)
    if sPaging:
        log.info("Start Multicast Paging OK.")
    else:
        log.info("Start Multicast Paging Failed, Retry Now.")
        multicastPaing(phoneA, phoneB)
    time.sleep(3)

    ePaging = phoneA.press_key('f4')
    if ePaging:
        log.info("End Multicast Paging OK.")
    else:
        log.info("End Multicast Paging Failed, Retry Now.")
        multicastPaing(phoneA, phoneB)

    print("Multicast Paging %d times." % i)

    time.sleep(2)


for i in range(10000):
    multicastPaing(phoneA, phoneB)


