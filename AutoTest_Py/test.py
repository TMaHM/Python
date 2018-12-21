import os
import requests



url_test = 'http://user:1234@10.3.2.58/download_screen'
r = requests.get(url_test)
print(r.status_code)