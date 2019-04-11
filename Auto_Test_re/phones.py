import requests
import re
import os
import time

from configs import *
from status import *

screen_dir = './log/screenShot/'

class Phone():

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

    def dial(self, dst_ext, account='Account=1'):
        """
        Phone(A) dial Phone(B)'s extension
        :param dst_ext: str Destination Extension
        :param account: str Default account='Account=1'
        :return: True or False
        """

        check_dial = False
        # 定义拨号url，使用ActionURL方式拨号
        self.url_dial = self.url.prefix + '/Phone_ActionURL&Command=1&Number=' + dst_ext + '&' + account
        # print(self.url_dial)
        try:
            r_dial = requests.get(self.url_dial, timeout=2)
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
            r_answer = requests.get(self.url_answer, timeout=2)
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
            log.info(self.url_answer + ' Connection Error.')

        return check_answer

    def set_key(self, key, type, value, account='Account1', label=''):

        type = type.upper()
        value = value.upper()
        account = account.upper()

        pat_key_type = dsskey_dir[key]['type']
        pat_key_value = dsskey_dir[key]['value']
        pat_key_account = dsskey_dir[key]['account']
        pat_key_label = dsskey_dir[key]['label']

        pc_key_type = key_type_code_dir[type.upper()]
        pc_key_account = key_account_code_dir[account.upper()]

        pat_pv = r'(?<=<)(P\d+)'

        with open('cfg.xml', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for eachLine in lines:
                key_type = re.findall(pat_key_type, eachLine, flags=re.IGNORECASE)
                key_value = re.findall(pat_key_value, eachLine, flags=re.IGNORECASE)
                key_account = re.findall(pat_key_account, eachLine, flags=re.IGNORECASE)
                key_label = re.findall(pat_key_label, eachLine, flags=re.IGNORECASE)
                if key_type:
                    pv_key_type = re.findall(pat_pv, eachLine)[0]
                    self.url_set_key_type = self.url.setting + pv_key_type + '=' + pc_key_type
                if key_value:
                    pv_key_value = re.findall(pat_pv, eachLine)[0]
                    self.url_set_key_value = self.url.setting + pv_key_value + '=' + value
                if key_account:
                    pv_key_account = re.findall(pat_pv, eachLine)[0]
                    self.url_set_key_account = self.url.setting + pv_key_account + '=' + pc_key_account
                if key_label:
                    pv_key_label = re.findall(pat_pv, eachLine)[0]
                    self.url_set_key_label = self.url.setting + pv_key_label + '=' + label

        try:
            r_key_type = requests.get(self.url_set_key_type, timeout=2)
            r_key_value = requests.get(self.url_set_key_value, timeout=2)
            r_key_account = requests.get(self.url_set_key_account, timeout=2)
            if label != '':
                r_key_label = requests.get(self.url_set_key_label, timeout=2)
                if r_key_label.status_code != 200:
                    log.info(self.ip + ' set label failed.')
                else:
                    pass
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
            r_pr = requests.get(self.url_press_key, timeout=2)
            if r_pr.status_code == 200:
                time.sleep(1)
                log.info(self.ip + ' press ' + cmd)
            else:
                log.info(self.ip + ' press ' + cmd + ' failed...')

        except requests.exceptions.ConnectionError:
            log.info(self.url_end + ' Connection Error.')

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
            if mod == 'AT' or mod == 'SAT':
                self.press_key('pound')
            elif mod == 'BT':
                self.press_key('f_transfer')
            else:
                log.info('Transfer mod error --> ' + mod)


    def exp_blf(self, cmd):
        for k, v in exp_blf_dir.items():

            if cmd.upper() != k:
                continue
            elif cmd.upper() == k:
                self.url_exp_key = self.url.keyboard + v
                try:
                    r_exp_key = requests.get(self.url_exp_key, timeout=2)
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
            r_end = requests.get(self.url_end, timeout=2)
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
            r_mem = requests.get(self.url_memory, timeout=2)
            if r_mem.status_code == 200:
                check_get_memory = True
                mem_info = re.findall(pat_untag, r_mem.text)
                log.info(self.ip + str(mem_info))
            else:
                log.info(self.ip + 'Get memory failed, return ' + str(r_mem.status_code))
        except requests.exceptions.ConnectionError:
            log.info(self.url_memory + ' Connection Error.')

        return check_get_memory

    def screen_shot(self, screen_name):
        """
        Capture the LCD screenShot when check status returns False
        :param screenpath:
        :return:
        """

        retry = 0
        check_screen_shot = False

        self.url_screen_shot = self.url.screenshot
        try:
            while retry < 2:
                r_screen_shot = requests.get(self.url_screen_shot, timeout=5)
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


for i in range(num_dut):
    p_list.append(Phone(ip_list[i], ext_list[i]))
