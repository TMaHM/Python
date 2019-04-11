import requests
import re

ip1 = '10.1.2.24'
ip2 = '10.1.2.19'
ip3 = '10.1.2.30'
ip4 = '10.1.2.6'
ip5 = '10.1.2.14'
ip6 = '10.1.2.15'
ip7 = '10.1.2.25'
ip8 = '10.1.2.7'
ip9 = '10.1.2.12'
ip10 = '10.1.2.28'
ip11 = '10.1.2.43'
ip12 = '10.1.2.18'
ip13 = '10.1.2.27'
ip14 = '10.1.2.16'
ip15 = '10.1.2.17'
ip16 = '10.1.2.35'
ip17 = '10.1.2.31'
ip18 = '10.1.2.13'
ip19 = '10.1.2.32'
ip20 = '10.1.2.33'
ip21 = '10.1.2.9'

ip_list = [ip1, ip2, ip3, ip4, ip5, ip6, ip7, ip8, ip9, ip10, ip11, ip12, ip13, ip14, ip15, ip16, ip17, ip18, ip19, ip20, ip21]

pat = r'ROM--\d+.*?\)'

for ip in ip_list:
    url = 'http://admin:admin@' + ip + '/index.htm'
    r = requests.get(url)
    # print(r.content)
    rom = re.findall(pat, str(r.content))
    print(ip + ': ' + str(rom))