import requests

# ip1 = '192.168.1.38'
# ip2 = '192.168.1.60'
# ip3 = '192.168.2.1'
# ip4 = '192.168.1.58'
# ip5 = '192.168.1.35'
# ip6 = '192.168.1.72'
# ip7 = '192.168.1.123'
# ip8 = '192.168.1.28'
# ip9 = '192.168.1.75'
# ip10 = '192.168.1.44'
ip1 = '192.168.22.27'
ip2 = '192.168.22.203'
ip3 = '192.168.22.159'
ip4 = '192.168.22.5'
ip5 = '192.168.22.204'
ip6 = '192.168.22.214'
ip7 = '192.168.22.33'
ip8 = '192.168.1.28'
ip9 = '192.168.1.41'

ip_list = [ip1, ip2, ip3, ip4, ip5, ip6, ip7, ip8, ip9, ]
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
