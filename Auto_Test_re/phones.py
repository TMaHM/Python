import requests
import re
import os
import time

from configs import *
from status import *

screen_name = init_log('info')

class Phone():

    def __init__(self, ip, extension=None, usr='admin', pwd='admin'):
        """
        Initializing the Phone's IP, Extension, Web usrname and Web password
        and import class Url() use for getting the AutoTest URL
        :param ip: str Phone's IP
        :param extension: str Phone's Extension
        :param usr: str Phone's web usrname
        :param pwd: str Phone's web password
        """
        self.ip = ip
        self.ext = extension
        self.usr = usr
        self.pwd = pwd
        self.url = Test_Url(self.ip, self.usr, self.pwd)


    def dial(self, dst_ext, account='Account=1'):
        """
        Phone(A) dial Phone(B)'s extension
        :param dst_ext: str Destination Extension
        :param account: str Defalut account='Account=1'
        :return: True or False
        """

        check_dial = False
        # 定义拨号url，使用ActionURL方式拨号
        self.url_dial = self.url.prefix + '/Phone_ActionURL&Command=1&Number=' + dst_ext + '&' + account
        # print(self.url_dial)
        try:
            r_dial = requests.get(self.url_dial, timeout=1)
            if r_dial.status_code == 200:
                log.info(self.ip + ' dial ' + dst_ext)
                time.sleep(1)
                if check_status('outgoing', self.ip):
                    check_dial = True
                    log.info('Dial ' + dst_ext + ' success.')
                else:
                    self.screen_shot()
                    log.info(self.ip + ' dial failed.')
            else:
                log.info(self.ip + ' Return ' + str(r_dial.status_code) + ', Dial Failed.')

        except requests.exceptions.ConnectionError:
            log.info(self.url_dial + ' Connection Error.')

        return check_dial


    def answer(self, cmd):
        """
        Phone(A) answers the call
        :param cmd: str F1, SPEAKER or OK
        :return: True or False
        """

        check_answer = False
        self.url_answer = self.url.keyboard + cmd.upper()
        try:
            r_answer = requests.get(self.url_answer, timeout=1)
            if r_answer.status_code == 200:
                log.info(self.ip + ' press ' + cmd + ' to answer.')
                time.sleep(1)
                # 验状态失败不一定执行失败，再看截图
                if check_status('talking', self.ip):
                    check_answer = True
                    log.info(self.ip + ' answered the call with ' + cmd)
                else:
                    self.screen_shot()
                    log.info(self.ip + ' answer maybe failed.')
            else:
                log.info(self.ip + ' Return ' + str(r_answer.status_code) + ', Answer Failed.')
        except requests.exceptions.ConnectionError:
            log.info(self.url_answer + ' Connection Error.')

        return check_answer

    def set_key(self, key, type, value, account='Account1'):

        key = key.upper()
        type = type.upper()
        value = value.upper()
        account = account.upper()

        # 找到key对应的三个P值：type/value/account
        pv_key_type = dss_key_dir['key_Pvalue'][key]['type']
        pv_key_value = dss_key_dir['key_Pvalue'][key]['value']
        pv_key_account = dss_key_dir['key_Pvalue'][key]['account']

        # 找到key_type对应的code
        pc_key_type = dss_key_dir['type_Code'][type]

        # 找到account对应的code
        pc_key_account = dss_key_dir['account_Code'][account]

        self.url_set_key_type = self.url.setting + pv_key_type + '=' + pc_key_type
        self.url_set_key_value = self.url.setting + pv_key_value + '=' + value
        self.url_set_key_account = self.url.setting + pv_key_account + '=' + pc_key_account

        try:
            r_key_type = requests.get(self.url_set_key_type, timeout=1)
            r_key_value = requests.get(self.url_set_key_value, timeout=1)
            r_key_account = requests.get(self.url_set_key_account, timeout=1)
            if (r_key_type.status_code and r_key_value.status_code and r_key_account.status_code) == 200:
                log.info(self.ip + ' set ' + key + ' as ' + type + ' success.')
            else:
                log.info(self.ip + ' set ' + key + ' as ' + type + ' failed...')
                log.info('check url:\n' + self.url_set_key_type + '\n' + self.url_set_key_value + '\n' + self.url_set_key_account)

        except requests.exceptions.ConnectionError:
            log.info(self.ip + ' connection error.')


    def press_key(self, cmd):
        self.url_press_key = self.url.keyboard + cmd.upper()
        try:
            r_pr = requests.get(self.url_press_key, timeout=1)
            if r_pr.status_code == 200:
                time.sleep(1)
                log.info(self.ip + ' press ' + cmd)
            else:
                log.info(self.ip + ' press ' + cmd + ' failed...')

        except requests.exceptions.ConnectionError:
            log.info(self.url_end + ' Connection Error.')

    def exp_blf(self, cmd):
        for k,v in exp_blf_dir.items():

            if cmd.upper() != k:
                continue
            elif cmd.upper() == k:
                self.url_exp_key = self.url.keyboard + v
                try:
                    r_exp_key = requests.get(self.url_exp_key, timeout=1)
                    if r_exp_key.status_code == 200:
                        time.sleep(1)
                        log.info(self.ip + ' trigger Expansion ' + cmd)
                        return True
                    else:
                        log.info(self.ip + ' trigger Expansion' + cmd + 'failed...')
                except requests.exceptions.ConnectionError:
                    log.info(self.url_exp_key + ' Connection Error.')


    def end_call(self, cmd):
        """
        Phone(A) end the call.
        :param cmd: str F4, SPEAKER or X
        :return: True or False
        """

        check_end = False
        self.url_end = self.url.keyboard + cmd.upper()
        try:
            r_end = requests.get(self.url_end, timeout=1)
            if r_end.status_code == 200:
                time.sleep(1)
                if check_status('idle', self.ip):
                    check_end = True
                    log.info(self.ip + ' The call ended with ' + cmd)
                else:
                    self.screen_shot()
                    log.info(self.ip + ' end call failed with ' + cmd)
            else:
                log.info(self.ip + ' Return ' + str(r_end.status_code) + ', End call failed.')
        except requests.exceptions.ConnectionError:
            log.info(self.url_end + ' Connection Error.')

        return check_end


    def get_memory(self):
        """
        Get Phone(A)'s memory info
        :return: True or False
        """

        check_get_memory = False
        pat_untag = r'(?<=\>)(.*)(?=\<)'
        self.url_memory = self.url.get_memory
        try:
            r_mem = requests.get(self.url_memory, timeout=1)
            if r_mem.status_code == 200:
                check_get_memory = True
                mem_info = re.findall(pat_untag, r_mem.text)
                log.info(self.ip + str(mem_info))
            else:
                log.info(self.ip + 'Get memory failed, return ' + str(r_mem.status_code))
        except requests.exceptions.ConnectionError:
            log.info(self.url_memory + ' Connection Error.')

        return check_get_memory


    def screen_shot(self):
        """
        Capture the LCD screenshot when check status returns False
        :param screenpath:
        :return:
        """

        retry = 0
        check_screen_shot = False

        self.url_screen_shot = self.url.screenshot
        try:
            while retry < 2:
                r_screen_shot = requests.get(self.url_screen_shot, timeout=1)
                if r_screen_shot.status_code == 200:
                    cur_time = time.strftime("%m%d_%H%M%S", time.localtime())
                    stored_screen = screen_name + cur_time + '.jpg'
                    with open(stored_screen, 'wb') as f:
                        f.write(r_screen_shot.content)
                        check_screen_shot = True
                        log.info('Capture Screenshot Success: ' + stored_screen)
                        break
                elif r_screen_shot.status_code == 401:
                    log.info('Capture Screenshot return ' + str(r_screen_shot.status_code) + ' will try agian.')
                    retry += 1
                    continue
            else:
                log.info('Capture Screenshot failed.')
        except requests.exceptions.ConnectionError:
            log.info('Connection Error. Capture Screenshot failed.')

        return check_screen_shot


for i in range(num_dut):
    p_list.append(Phone(ip_list[i], ext_list[i]))
