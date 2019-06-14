import requests
import time

multicastPaging = "http://admin:admin@10.3.2.47/AutoTest&keyboard=L14"

endPaging= "http://admin:admin@10.3.2.47/AutoTest&keyboard=F4"

for i in range(10000):

    sPaging = requests.get(multicastPaging)

    time.sleep(3)

    ePaging = requests.get(endPaging)

    time.sleep(2)

    print(i)