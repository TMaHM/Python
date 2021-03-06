import requests

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
# ip1 = '192.168.22.27'
# ip2 = '192.168.22.203'
# ip3 = '192.168.22.159'
# ip4 = '192.168.22.5'
# ip5 = '192.168.22.204'
# ip6 = '192.168.22.214'
# ip7 = '192.168.22.33'
# ip8 = '192.168.1.28'
# ip9 = '192.168.1.41'

ip_list = [ip1, ip2, ip3, ip4, ip5, ip6, ip7, ip8, ip9, ip10, ip11, ip12, ip13, ip14, ip15, ip16, ip17, ip18, ip19, ip20, ip21]
num = int(input('Enter the number need to be upgrade: '))

upgrade_ip = ip_list[:num]

fw_path = input('Please enter the fw_path: ')

cnt = 0

with open(r'F:\Project\AutoTestTools\Auto_Test_re\log\upgrade.log', 'a+', encoding='utf-8') as f:
    for ip in upgrade_ip:
        cnt += 1
        url_gen = 'http://admin:admin@' + ip + '/AutoTest&setting='
        url_pnp = url_gen+ 'P20165=0'  # disable pnp
        url_up_mode = url_gen + 'P212=1'  # set upgrade mode as http
        url_fw_path = url_gen + 'P192=' + fw_path
        url_cfg_path = url_gen + 'P237='  # config path置空，防止指派server修改fw_path
        url_override = url_gen + 'P145=0'  # disable option66 override
        url_on_ftp = url_gen + 'P8671=1'  # enable ftp
        url_on_telnet = url_gen + 'P8670=1'  # enable telnet
        try:
            r_pnp = requests.get(url_pnp)
            f.write(str(r_pnp.status_code) + '\n')
            print('1')

            r_mode = requests.get(url_up_mode)
            f.write(str(r_mode.status_code) + '\n')
            print('2')

            r_fw_path = requests.get(url_fw_path)
            f.write(str(r_fw_path.status_code) + '\n')
            print('3')

            r_cfg_path = requests.get(url_cfg_path)
            f.write(str(r_cfg_path.status_code) + '\n')
            print('4')

            r_op = requests.get(url_override)
            f.write(str(r_op.status_code) + '\n')
            print('5')

            r_ftp = requests.get(url_on_ftp)
            f.write(str(r_ftp.status_code) + '\n')
            print('6')

            r_tel = requests.get(url_on_telnet)
            f.write(str(r_tel.status_code) + '\n')
            print('7')

            reboot = 'http://admin:admin@' + ip + '/AutoTest&keyboard=Reboot'
            r_reboot = requests.get(reboot)
            f.write(str(r_reboot.status_code) + '\n')
            print('8')

            print("Upgrade times " + str(cnt))

        except requests.exceptions.ConnectionError:
            print(ip + 'ConnectionError.')
            f.write(ip + 'ConnectionError.\n')
