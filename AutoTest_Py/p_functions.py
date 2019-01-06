import time
import requests
import re
import os
import logging as log
from PyQt5.QtCore import QTime

import configurations as conf


class PhoneFunction():
    """
    进行实例化时，需要一个参数：cur_exec_file,即当前执行文件的文件名，由os.path.basename(__file__)提供
    Usage::

        >>> import os
        >>> from p_functions import PhoneFunction
        >>> ip = '10.3.2.10'
        >>> cur_exec_file = os.path.basename(__file__)
        >>> pf = PhoneFunction(cur_exec_file)
        >>> pf.idle_state_set(ip)
        >>> pf.check_status(ip, 'speaker')
    """

    def __init__(self, cur_exec_file, log_level='info'):
        """设置全局变量"""
        # 当前执行文件的文件名
        self.cur_exec_file = cur_exec_file
        # 当前所在目录的路径
        self.root_path = os.path.dirname(__file__)
        # 去除文件名后缀，用作建立当前执行文件的log存放目录
        self.cur_exec_file_nosuffix = re.split(r'\.', self.cur_exec_file)[0]
        # log及截屏文件存放目录
        self.log_dir_path = self.root_path + '\\log\\' + self.cur_exec_file_nosuffix + '\\'
        # log文件绝对路径
        self.log_file = self.log_dir_path + self.cur_exec_file_nosuffix + '.log'
        if not os.path.exists(self.log_dir_path):
            os.makedirs(self.log_dir_path)

        if log_level == 'debug':
            log.basicConfig(level=log.DEBUG,
                            format='%(asctime)s [%(levelname)s] %(message)s',
                            datefmt='%b %d %H:%M:%S',
                            filename=self.log_file,
                            filemode='a')
        elif log_level == 'info':
            log.basicConfig(level=log.INFO,
                            format='%(asctime)s [%(levelname)s] %(message)s',
                            datefmt='%b %d %H:%M:%S',
                            filename=self.log_file,
                            filemode='a')

    def idle_state_set(self, ip):
        """将话机置为idle态，需要一个参数:话机IP，参数类型：string\n
        返回值为 True / False
        Usage::

            >>> ip = '10.3.2.10'
            >>> cur_exec_file = os.path.basename(__file__)
            >>> pf = PhoneFunction(cur_exec_file)
            >>> pf.idle_state_set(ip)
        """

        url_keyboard = conf.Url(ip).url_keyboard
        url_f4 = url_keyboard + 'F4'
        url_x = url_keyboard + 'X'

        log.info(ip + ' try to return to [Idle] status...')
        try:
            r1 = requests.get(url_f4, timeout=5)
            log.info('Press F4 Response: ' + str(r1.status_code))
            time.sleep(conf.sleep_time())
            r2 = requests.get(url_x, timeout=5)
            log.info('Press X Response: ' + str(r2.status_code))
            if (r1 and r2) == 200:
                log.info('Operation successfully, will check the status...')
            check_status = self.check_status(ip, 'idle')
            if check_status:
                return True
            else:
                return False

        except requests.exceptions.ConnectionError:
            log.info('Connect Error...')
            log.info('Please check the url ' + url_f4)
            return False

    def check_status(self, ip, status):
        """检查话机当前状态，需要两个参数：话机IP和需检查的status，参数类型:string\n
        返回值：True / False\n
        只有r.status返回200，并且check状态ok时，check_result返回True \n
        Usage::

            >>> ip = '10.3.2.10'
            >>> status = 'idle'
            >>> check_status(ip, status)

        Depending on the check result, there are two different format of the response,
        
        Error::
            <html>
            <Return>1</Return>
            <FXS>1 FXSState=0x81</FXS>
            <CallCtl>1 CallCtlState=0x61</CallCtl>
            <LCM>1 LCMState=4 </LCM>
            </html>
        
        Success::
            <html>
            <Return>0</Return>
            <FXS>0</Return>
            <CallCtl>0</CallCtl>
            <LCM>0</LCM>
            </html>
        """

        # Define the phone status dict for returning status code for which the check status should be.
        phone_status_dir = {
            'idle': [{'code': '0'},
                     {'FXSState': '0x80', 'CallCtlState': '0x60',
                      'LCMState': '-1'}],
            'speaker': [{'code': '1'},
                        {'FXSState': '0x81', 'CallCtlState': '0x61',
                         'LCMState': '4'}],
            'outgoing': [{'code': '2'},
                         {'FXSState': '0x82', 'CallCtlState': '0x62',
                          'LCMState': '5'}],
            'talking': [{'code': '3'},
                        {'FXSState': '0x82', 'CallCtlState': '0x64',
                         'LCMState': '6'}],
            'ringing': [{'code': '4'},
                        {'FXSState': '0x82', 'CallCtlState': '0x63',
                         'LCMState': '3'}],
            'hold': [{'code': '5'},
                     {'FXSState': '0x82', 'CallCtlState': '0x87',
                      'LCMState': '7'}],
            'new_initiate': [{'code': '6'},
                             {'FXSState': '0x82', 'CallCtlState': '0x81',
                              'LCMState': '11'}],
            'new_talking': [{'code': '7'},
                            {'FXSState': '0x82', 'CallCtlState': '0x82',
                             'LCMState': '6'}],
            'conference': [{'code': '8'},
                           {'FXSState': '0x82', 'CallCtlState': '0x88',
                            'LCMState': '9'}],
            'conf_held': [{'code': '9'},
                          {'FXSState': '0x82', 'CallCtlState': '0x8d',
                           'LCMState': '9'}],
            'check_ok': [{'code': '0'},
                         {'FXS': '0', 'CallCtl': '0', 'LCM': '0'}],
        }

        pattern_status = r'<([a-zA-Z]+)>(.*)</\1>'
        # 当r.status返回200，并且check状态ok时，check_result返回True
        check_result = False

        need_check = phone_status_dir[status][0]['code']
        cur_status_dir = {}
        warning_list = []

        url_check = conf.Url(ip).url_check_status + need_check
        try:
            r = requests.get(url_check, timeout=5)
            if r.status_code == 200:
                status_get = re.findall(pattern_status, r.text)
                if status_get:
                    # status_get = [('CallCtl', '0')],这是一个列表，元素为一个元组
                    # 取出元组后再处理，each_status = ('CallCtl', '0')
                    # check_entry = CallCtl; cur_status = 0
                    for each_status in status_get:
                        check_entry = each_status[0]
                        cur_status = re.split(r'\s', each_status[1])
                        if check_entry == 'Return':
                            if cur_status[0] == '0':
                                check_result = True
                                log.info(ip + ' ' + status.title() + 'status check success...')

                            elif cur_status[0] == '1':
                                log.info(ip + ' ' + status.title() + ' status check error...')
                                log.debug(r.text)
                                self.down_screenshot(ip, status)
                        else:
                            if cur_status[0] == '0':
                                cur_status_dir[check_entry] = cur_status[0]
                                log.debug(
                                    ip + ' ' + check_entry + ' status check success...')
                            elif cur_status[0] == '1':
                                cur_status_disc = re.split(r'=', cur_status[1])[0]
                                cur_status_code = re.split(r'=', cur_status[1])[1]
                                cur_status_dir[cur_status_disc] = cur_status_code
                                warning_content = cur_status[1] + ' --> should be ' + \
                                                  phone_status_dir[status][1][cur_status_disc]
                                warning_list.append(warning_content)
                    dir_match = 0
                    for key, value in phone_status_dir.items():
                        if value[1] == cur_status_dir:
                            dir_match += 1
                            log.debug('The current status is [' + key.title() + ']')
                    if dir_match == 0:
                        log.info('The current status cannot match to any status...')
                        log.info(str(cur_status_dir))
                        # log.info('\n' + str(r.text))
                    for warning in warning_list:
                        log.info(warning)

            else:
                log.info(
                    'Check status failed because request return ' + r.status_code)

        except requests.exceptions.ConnectionError:
            log.info('Connect error, please check the url: ' + url_check)

        return check_result

    def down_screenshot(self, ip, status):
        """用于在check status失败时对话机截屏，不需要主动调用"""

        url_screenshot = conf.Url(ip).url_screenshot
        try:
            r = requests.get(url_screenshot, timeout=2)
            if r.status_code == 200:
                screenshot_time = re.sub(r':', '', QTime.currentTime().toString())
                screenshot_named = self.log_dir_path + 'Check' + status + 'Error' + screenshot_time + '.jpg'
                with open(screenshot_named, 'wb') as f:
                    f.write(r.content)
                    f.close()
            elif r.status_code == 401:
                log.info('Capture screen return 401, will try again.')
                r = requests.get(url_screenshot, timeout=2)
                if r.status_code == 200:
                    log.info('Screenshot has been captured in ' + self.log_file)
                    screenshot_time = re.sub(r':', '', QTime.currentTime().toString())
                    screenshot_named = self.log_dir_path + 'Check' + status + 'Error' + screenshot_time + '.jpg'
                    with open(screenshot_named, 'wb') as f:
                        f.write(r.content)
                        f.close()
                else:log.info('Try capture screen 2nd times failed, please check the pwd.')
            else:
                log.info(
                    'Cannot capture screen now because requests return ' + str(
                        r.status_code))

        except requests.exceptions.ConnectionError:
            log.info('Connect ' + ip + ' Error...')
            log.info('Download screenshot from ' + ip + ' failed...')

    def get_memory(self, ip):
        """用于获取话机当前内存，需要一个参数：IP\n
        Usage::
            >>> Phone_Function.get_memory(ip)
        """

        url_get_memory = conf.Url(ip).url_get_memory
        pattern_memory = r'(?<=MemoryFree>).*(?=</MemoryFree>)'

        try:
            r = requests.get(url_get_memory, timeout=5)
            if r.status_code == 200:
                memory_free = re.search(pattern_memory, r.text).group()
                log.info(ip + ' ' + memory_free)

            else:
                log.info(
                    'Get MemoryFree Failed because requests return ' + str(
                        r.status_code))

        except requests.exceptions.ConnectionError:
            log.info('Connect error, please check the url: ' + url_get_memory)

    def dial(self, ip, extension, Account='1'):
        """采用ActionURL拨号，需要3个参数，caller IP， called Extension，caller Account(默认为Account1) \n
        ActionURL的格式为：http://admin:admin@192.168.0.124/Phone_ActionURL&Command=1&Number=206&Account=1 \n
        Usage::
            >>> dial(caller_IP, called_extension)
            >>> dial(caller_IP, called_extension, Account=2)
        """
        # url_speaker = conf.Url(ip).url_keyboard + 'SPEAKER'
        if Account == '1':
            url_dial = conf.Url(ip, number=extension).url_dial
        elif Account:
            url_dial = conf.Url(ip, account='&Account=' + Account,
                                number=extension).url_dial

        try:
            # r_sp = requests.get(url_speaker, timeout=5)
            r_dial = requests.get(url_dial, timeout=5)
            if r_dial.status_code == 200:
                log.info('Account' + Account + ' dial ' + extension)

            elif r_dial.status_code == 401:
                warning_content = 'Cannot dial now...Authentication Failed because requests return ' + str(
                    r_dial.status_code)
                log.info(warning_content)
                log.info('Will try another pwd...')

                # if Account == '1':
                #     url_dial_again = conf.Url(ip, number=extension,
                #                               pwd='222222').url_dial
                # else:
                #     url_dial_again = conf.Url(ip, account='&Account' + Account,
                #                               number=extension).url_dial
                # try:
                #     r = requests.get(url_dial_again)
                #     if r.status_code == 200:
                #         log.info('Try pwd:222222 success...')
                #         log.info('Account' + Account + ' dial ' + extension)

                #     elif r.status_code == 401:
                #         warning_content = 'Cannot dial now Authenticantion Failed again because requests return ' + str(
                #             r.status_code)
                #         log.info(warning_content)

                # except requests.exceptions.ConnectionError:
                #     log.info(
                #         'Connect error, please check the url: ' + url_dial)
                #         return False

            else:
                log.info('Dialing Failed with unknown reason...')

        except requests.exceptions.ConnectionError:
            log.info('Connect error, please check the url: ' + url_dial)


    def answer(self, ip_B, ip_A):
        """需要两个参数：called的IP在前，caller的IP在后\n
        根据answer后，check talking status的结果返回 True / False\n
        Usage::
            >>> answer(ip)
        """

        url_answer = conf.Url(ip_B).url_keyboard + 'F1'
        check_answer = False

        try:
            r = requests.get(url_answer, timeout=5)

            if r.status_code == 200:
                log.info(ip_B + ' Press F1 to answer the call...')
                time.sleep(1)
                if self.check_status(ip_B, 'talking'):
                    if self.check_status(ip_A, 'talking'):
                        log.info(ip_A + ' and ' + ip_B + ' [talking] status '
                                                       'check ok...')
                        log.info(ip_B + ' answered...')
                        check_answer = True
                        return check_answer
                    else:
                        log.info(ip_A + ' talking status check error...')
                        return check_answer
                else:
                    log.info(ip_B + ' talking status check error...answered '
                                    'failed...')
                    return check_answer

            elif r.status_code == 401:
                log.info(
                    ip_B + ' answered failed because requests return ' + str(
                        r.status_code))
                return check_answer

            else:
                log.info(
                    ip_B + ' answered failed because requests return ' + str(
                        r.status_code))
                return check_answer

        except requests.exceptions.ConnectionError:
            log.info(
                ip_B + ' connect error, please check the url: ' + url_answer)
            return check_answer


    def endcall(self, ip_A, ip_B, cmd='F4'):
        """需要3个参数：执行EndCall的IP在前，对端(check idle status)的IP在后,最后是cmd='F4'或'SPEAKER,默认为F4'\n
        当执行EndCall后，根据check idle status的结果返回 True / False \n
        Usage::
            >>> endcall(ip_A, ip_B)
            >>> endcall(ip_A, ip_B, 'SPEAKER')
        """

        url_endcall = conf.Url(ip_A).url_keyboard + cmd
        check_endcall = False

        try:
            r = requests.get(url_endcall, timeout=5)
            if r.status_code == 200:
                log.info(ip_A + ' Press ' + cmd + ' to endcall')
                time.sleep(1)
                if self.check_status(ip_A, 'idle'):
                    if self.check_status(ip_B, 'idle'):
                        log.info(ip_A + ' and ' + ip_B + ' [Idle] status '
                                                       'check ok...')
                        log.info(ip_A + ' ended the call...')
                        check_endcall = True
                        return check_endcall
                    else:
                        log.info(ip_B + ' is not in [Idle] status...')
                else:
                    log.info(ip_A + ' is not in [Idle] status...')
                    return check_endcall

            elif r.status_code == 401:
                log.info(ip_A + ' endcall failed because requests return ' +
                         str(r.status_code))
                return check_endcall

            else:
                log.info(
                    ip_A + ' endcall failed because requests return ' + str(
                        r.status_code))
                return check_endcall

        except requests.exceptions.ConnectionError:
            log.info(
                ip_A + ' connect error, please check the url: ' + url_endcall)
            return check_endcall

    def test_call(self, ip, cmd=None, ext=None):
        """执行test call，需要3个参数，执行命令的话机IP，Dst. Extension Number, command,默认为'p'\n
        Usage::
            >>> Phone_Function(self.cur_exec_file).test_call('10.10.2.2', 's')
            >>> Phone_Function(self.cur_exec_file).test_call('10.10.3.3', ext='3050')
        """

        if cmd is None and ext is not None:
            url_tc = conf.Url(ip).url_setting + 'P4210=' + 'test' + ext
            try:
                r = requests.get(url_tc)
                print(r.status_code)
            except requests.exceptions.ConnectionError:
                print('Connect Error...Please check the url: ' + url_tc)

        elif cmd == 's':
            url_tc = conf.Url(ip).url_setting + 'P4210=' + ''
            try:
                r = requests.get(url_tc)
                print(r.status_code)
            except requests.exceptions.ConnectionError:
                print('Connect Error...Please check the url: ' + url_tc)

        else:
            print('Param Error...')
