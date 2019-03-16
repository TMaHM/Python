import requests
import time

cnt = 0

while True:
    r1 = requests.get("http://admin:admin@10.3.2.180/AutoTest&keyboard=L2")
    time.sleep(3)

    r2 = requests.get("http://admin:admin@10.3.2.168/AutoTest&keyboard=F1")
    time.sleep(3)

    r3 = requests.get("http://admin:admin@10.3.2.168/AutoTest&keyboard=EXPANSION:EXP_NO:0EXP_PAGE:0EXP_KEYNO:0")
    time.sleep(2)

    r4 = requests.get("http://admin:admin@10.3.2.3/AutoTest&keyboard=F1")
    time.sleep(5)

    r5 = requests.get("http://admin:admin@10.3.2.180/AutoTest&keyboard=F4")
    time.sleep(3)

    cnt += 1
    print(cnt)
