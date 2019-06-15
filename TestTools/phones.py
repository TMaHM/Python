import time

from status import *

screen_dir = './log/screenShot/'


class Phone(object):

    def __init__(self, ip, extension=None, usr='admin', pwd='admin'):
        """
        Initializing the Phone's IP, Extension, Web username and Web password
        and import class Url() use for getting the AutoTest URL
        :param ip: str Phone's IP
        :param extension: str Phone's Extension
        :param usr: str Phone's web username
        :param pwd: str Phone's web password
        """
        self.ip = ip
        self.ext = extension
        self.usr = usr
        self.pwd = pwd
        self.url = TestUrl(self.ip, self.usr, self.pwd)
        self.cfg_file = 'cfg%s.xml' % self.ip.replace('.', '_')

        if not os.path.exists(self.cfg_file):
            print('Preparing configuration files, please wait...')
            with open(self.cfg_file, 'a', encoding='utf-8') as f:
                log.info('Try to download %s' % self.cfg_file)
                return_code = requests.get('http://%s:%s@%s/download_xml_cfg' % (self.usr, self.pwd, ip)).status_code
                if return_code == 200:
                    file_content = requests.get(
                            'http://%s:%s@%s/download_xml_cfg' % (self.usr, self.pwd, ip)).content.decode()
                    f.write(file_content)
                    log.info('Download %s success.' % self.cfg_file)
                    print('Configuration file prepared.')
                elif return_code == 401:
                    log.info('Try download %s again.' % self.cfg_file)
                    file_content = requests.get(
                            'http://%s:%s@%s/download_xml_cfg' % (self.usr, self.pwd, ip)).content.decode()
                    f.write(file_content)
                    log.info('Download %s success.' % self.cfg_file)
                    print('Configuration file prepared.')

    def dial(self, dst_ext, account='Account=1'):
        """
        Phone(A) dial Phone(B)'s extension
        :param dst_ext: str Destination Extension
        :param account: str Default account='Account=1'
        :return: True or False
        """

        check_dial = False
        # 定义拨号url，使用ActionURL方式拨号
        url_dial = self.url.prefix + '/Phone_ActionURL&Command=1&Number=' + dst_ext + '&' + account
        # print(url_dial)
        try:
            r_dial = requests.get(url_dial, timeout=2)
            if r_dial.status_code == 200:
                log.info(self.ip + ' dial ' + dst_ext)
                time.sleep(1)
                if check_status('outgoing', self.ip):
                    check_dial = True
                    log.info('Dial ' + dst_ext + ' success.')
                else:
                    self.screen_shot('dial')
                    log.info(self.ip + ' dial failed.')
            else:
                log.info(self.ip + ' Return ' + str(r_dial.status_code) + ', Dial Failed.')

        except requests.exceptions.ConnectionError:
            log.info(url_dial + ' Connection Error.')

        return check_dial

    def answer(self, cmd):
        """
        Phone(A) answers the call
        :param cmd: str F1, SPEAKER or OK
        :return: True or False
        """

        check_answer = False
        url_answer = self.url.keyboard + cmd.upper()
        try:
            r_answer = requests.get(url_answer, timeout=2)
            if r_answer.status_code == 200:
                log.info(self.ip + ' press ' + cmd + ' to answer.')
                time.sleep(1)
                # 验状态失败不一定执行失败，再看截图
                if check_status('talking', self.ip):
                    check_answer = True
                    log.info(self.ip + ' answered the call with ' + cmd)
                else:
                    self.screen_shot('answer')
                    log.info(self.ip + ' answer maybe failed.')
            else:
                log.info(self.ip + ' Return ' + str(r_answer.status_code) + ', Answer Failed.')
        except requests.exceptions.ConnectionError:
            log.info(url_answer + ' Connection Error.')

        return check_answer

    def get_line_key(self, key):
        """
        :param key: 指定要获取状态的LineKey，变量范围L1-L36
        :return: 返回指定的LineKey的属性字典
        :如L1->{'type': 'LINE', 'value': 'None', 'label': '8724 | Stephen Yu', 'account': 'ACCOUNT1'}
        """
        import linecache

        line_key_num = re.findall(r'\d+', key)
        if line_key_num:
            pat_lineKey = r'LineKey%s_Type' % line_key_num[0]
            pat_key_type = r'(?<=>).*(?=<)'
            with open(self.cfg_file, encoding='utf-8') as f:
                linesCnt = 0
                lines = f.readlines()
                for each_line in lines:
                    linesCnt += 1
                    if pat_lineKey in each_line:
                        matched_key_type_code = re.findall(pat_key_type, each_line)
                        matched_key_value = re.findall(pat_key_type, linecache.getline(self.cfg_file, linesCnt + 2))
                        if matched_key_value:
                            real_key_value = matched_key_value[0]
                        else:
                            real_key_value = None
                        matched_key_label = re.findall(pat_key_type, linecache.getline(self.cfg_file, linesCnt + 3))
                        if matched_key_label:
                            real_key_label = matched_key_label[0]
                        else:
                            real_key_label = None
                        matched_key_account = re.findall(pat_key_type, linecache.getline(self.cfg_file, linesCnt + 4))
                        break
                    else:
                        matched_key_type_code = None
        else:
            log.info('Input line key [ %s ] mismatches, need to check.' % key)

        if matched_key_type_code is not None:
            cnt = 0  # 遍历key type字典时计数，遍历到结束时仍没有匹配返回No such key
            real_key_type = None  # 查字典，返回匹配到的Line Key的类型
            real_key_account = None  # 查字典，返回匹配到的Line Account的类型
            for k, v in key_type_code_dir.items():
                if matched_key_type_code[0] == v:
                    cnt += 1
                    real_key_type = k
                else:
                    continue

            if cnt == 1:
                # 如果找到keyType，再找keyAccount，未找到的情况下返回默认的None
                for k, v in key_account_code_dir.items():
                    if matched_key_account[0] == v:
                        real_key_account = k
                    else:
                        continue

                key_property = {'type'   : '%s' % real_key_type,
                                'value'  : '%s' % real_key_value,
                                'label'  : '%s' % real_key_label,
                                'account': '%s' % real_key_account}
                log.info('Check LineKey_%s properties return: %s' % (line_key_num[0], key_property))
                return key_property

            elif cnt > 1:  # 应该不可能会在字典里找到两个一样的，这里加上作为防范
                log.info('Matched key type is not unique, need to check.')
                return 'Not Unique'

            elif cnt < 1:
                log.info("No key matched, need to check.")
                return 'No Suck Key.'

    def set_line_key(self, key, k_type, value, account='Account1', label=''):
        # 格式化 k_type 和 account 字符串，采用全大写形式
        keyTypeUpper = k_type.upper()
        accountUpper = account.upper()

        # 准备字符串用来在xml文件中匹配，找出传入的key对应的type/value/account/label所在的行
        # 例如LineKey1_Type
        pat_key_type = dsskey_dir[key]['type']
        pat_key_value = dsskey_dir[key]['value']
        pat_key_account = dsskey_dir[key]['account']
        pat_key_label = dsskey_dir[key]['label']

        # 准备字符串用来在找到的行中，将对应的P值找出
        pat_pv = r'(?<=<)(P\d+)'

        # 在key_type_code_dir和key_account_code_dir字典中找到传入的k_type和account对应的值
        # 如N/A - 0
        pc_key_type = key_type_code_dir[keyTypeUpper]
        pc_key_account = key_account_code_dir[accountUpper]

        with open('%s/cfg.xml' % os.path.dirname(__file__), 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for eachLine in lines:
                matched_key_type = re.findall(pat_key_type, eachLine, flags=re.IGNORECASE)
                if matched_key_type:
                    pv_key_type = re.findall(pat_pv, eachLine)[0]
                    url_set_key_type = self.url.setting + pv_key_type + '=' + pc_key_type
                    try:
                        r_key_type = requests.get(url_set_key_type, timeout=2)
                        if r_key_type.status_code == 200:
                            log.info('%s set %s as %s success.' % (self.ip, key, k_type))
                        else:
                            log.info('%s set %s as %s failed.' % (self.ip, key, k_type))
                    except requests.exceptions.ConnectionError:
                        log.info(self.ip + ' connection error.')

                key_value = re.findall(pat_key_value, eachLine, flags=re.IGNORECASE)
                if key_value:
                    pv_key_value = re.findall(pat_pv, eachLine)[0]
                    url_set_key_value = self.url.setting + pv_key_value + '=' + value
                    try:
                        r_key_value = requests.get(url_set_key_value, timeout=2)
                        if r_key_value.status_code == 200:
                            log.info('%s set %s value as %s success.' % (self.ip, key, value))
                        else:
                            log.info('%s set %s value as %s failed.' % (self.ip, key, value))
                    except requests.exceptions.ConnectionError:
                        log.info(self.ip + ' connection error.')

                key_account = re.findall(pat_key_account, eachLine, flags=re.IGNORECASE)
                if key_account:
                    pv_key_account = re.findall(pat_pv, eachLine)[0]
                    url_set_key_account = self.url.setting + pv_key_account + '=' + pc_key_account
                    try:
                        r_key_account = requests.get(url_set_key_account, timeout=2)
                        if r_key_account.status_code == 200:
                            log.info('%s set %s account as %s success.' % (self.ip, key, account))
                        else:
                            log.info('%s set %s account as %s success.' % (self.ip, key, account))
                    except requests.exceptions.ConnectionError:
                        log.info(self.ip + ' connection error.')

                key_label = re.findall(pat_key_label, eachLine, flags=re.IGNORECASE)
                if key_label:
                    pv_key_label = re.findall(pat_pv, eachLine)[0]
                    url_set_key_label = self.url.setting + pv_key_label + '=' + label
                    if label != '':
                        try:
                            r_key_label = requests.get(url_set_key_label, timeout=2)
                            if r_key_label.status_code != 200:
                                log.info(self.ip + ' set label failed.')
                            else:
                                pass
                        except requests.exceptions.ConnectionError:
                            log.info(self.ip + ' connection error.')

    def press_key(self, cmd):
        press_key_flag = False
        url_press_key = self.url.keyboard + cmd.upper()
        try:
            r_pr = requests.get(url_press_key, timeout=2)
            if r_pr.status_code == 200:
                # time.sleep(1)
                log.info(self.ip + ' press ' + cmd.upper())
                press_key_flag = True  # 如果成功，将标识置为True
            else:
                log.info(self.ip + ' press ' + cmd.upper() + ' failed...')
                return press_key_flag  # 失败，直接返回False

            return press_key_flag  # 返回被置为True的标识

        except requests.exceptions.ConnectionError:
            log.info(url_press_key + ' Connection Error.')

    def transfer(self, ext='', mod='BT'):
        if ext != '':
            self.press_key('f_transfer')
            for number in ext:
                self.press_key(number)
            if mod == 'AT' or mod == 'SAT':
                self.press_key('pound')
            elif mod == 'BT':
                self.press_key('f_transfer')
            else:
                log.info('Transfer mod error --> ' + mod)
        elif ext == '':
            self.press_key('f_transfer')

    def exp_blf(self, cmd):
        for k, v in exp_blf_dir.items():

            if cmd.upper() != k:
                continue
            elif cmd.upper() == k:
                url_exp_key = self.url.keyboard + v
                try:
                    r_exp_key = requests.get(url_exp_key, timeout=2)
                    if r_exp_key.status_code == 200:
                        time.sleep(1)
                        log.info(self.ip + ' trigger Expansion ' + cmd)
                        return True
                    else:
                        log.info(self.ip + ' trigger Expansion' + cmd + 'failed...')
                except requests.exceptions.ConnectionError:
                    log.info(url_exp_key + ' Connection Error.')

    def end_call(self, cmd):
        """
        Phone(A) end the call.
        :param cmd: str F4, SPEAKER or X
        :return: True or False
        """

        check_end = False
        url_end = self.url.keyboard + cmd.upper()
        try:
            r_end = requests.get(url_end, timeout=2)
            if r_end.status_code == 200:
                time.sleep(1)
                if check_status('idle', self.ip):
                    check_end = True
                    log.info(self.ip + ' The call ended with ' + cmd)
                else:
                    self.screen_shot('end_call')
                    log.info(self.ip + ' end call failed with ' + cmd)
            else:
                log.info(self.ip + ' Return ' + str(r_end.status_code) + ', End call failed.')
        except requests.exceptions.ConnectionError:
            log.info(url_end + ' Connection Error.')

        return check_end

    def set_idle_status(self):
        result = False

        url_return_idle = self.url.prefix + '/drd=RETURNIDLE'
        # log.info('Try to set [idle] status in ' + ip)
        try:
            r_return_idle = requests.get(url_return_idle, timeout=1)
            if r_return_idle.status_code == 200:
                log.info(self.ip + ' set [idle] status in ' + self.ip + ' success.')
                result = True
            elif r_return_idle.status_code == 404:
                log.info('%s has not merged, try press [SPEAKER] twice to return to idle.' % url_return_idle)
                self.press_key('speaker')
                time.sleep(0.5)
                self.press_key('speaker')
                time.sleep(2)
                if check_status('idle', self.ip):
                    log.info('Return to Idle status success.')
                else:
                    log.info('Return to Idle status failed.')
            else:
                log.info('%s return %s' % (url_return_idle, r_return_idle.status_code))
        except requests.exceptions.ConnectionError:
            log.info('Connect Error...Set [idle] status failed...')

        return result

    def get_memory(self):
        """
        Get Phone(A)'s memory info
        :return: True or False
        """

        check_get_memory = False
        pat_un_tag = r'(?<=\>)(.*)(?=\<)'
        url_memory = self.url.get_memory
        try:
            r_mem = requests.get(url_memory, timeout=2)
            if r_mem.status_code == 200:
                check_get_memory = True
                mem_info = re.findall(pat_un_tag, r_mem.text)
                log.info(self.ip + str(mem_info))
            else:
                log.info(self.ip + 'Get memory failed, return ' + str(r_mem.status_code))
        except requests.exceptions.ConnectionError:
            log.info(url_memory + ' Connection Error.')

        return check_get_memory

    def screen_shot(self, screen_name):
        """
        Capture the LCD screenShot when check status returns False
        :param screen_name: 在调用时传入
        :return: True or False
        """

        retry = 0
        check_screen_shot = False

        url_screen_shot = self.url.screenshot
        try:
            while retry < 2:
                r_screen_shot = requests.get(url_screen_shot)  # 此处不加timeout，以防截屏文件传输超时
                if r_screen_shot.status_code == 200:
                    cur_time = time.strftime("%m%d_%H%M%S", time.localtime())
                    stored_screen = screen_dir + screen_name + cur_time + '.jpg'
                    with open(stored_screen, 'wb') as f:
                        f.write(r_screen_shot.content)
                        check_screen_shot = True
                        log.info('Capture ScreenShot Success: ' + stored_screen)
                        break
                elif r_screen_shot.status_code == 401:
                    log.info('Capture ScreenShot return ' + str(r_screen_shot.status_code) + ' will try again.')
                    retry += 1
                    continue
            else:
                log.info('Capture ScreenShot failed.')
        except requests.exceptions.ConnectionError:
            log.info('Connection Error. Capture ScreenShot failed.')

        return check_screen_shot

# for i in range(num_dut):
#     p_list.append(Phone(ip_list[i], ext_list[i]))
