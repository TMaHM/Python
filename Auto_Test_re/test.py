import requests
import re


pattern = r'<([a-zA-Z]+)>(.*)</\1>'
pat_1 = r'(?<=<Return>)(\d)(?=</Return>)'
pat_2 = r'([a-zA-Z]+State=.*)(?=\<)'
r_status = requests.get('http://admin:admin@10.3.2.22/AutoTest&autoverify=STATE=1')
print(r_status.text)
r_test = re.findall(pat_2, r_status.text)
print(r_test)
return_status = re.findall(pat_1, r_status.text)
print(return_status)