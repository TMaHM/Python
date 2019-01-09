import requests
import re
import os
import time

from configs import *
from status import *


class Phone():

    def __init__(self, ip, extension=None, usr='admin', pwd='admin'):
        self.ip = ip
        self.ext = extension
        self.usr = usr
        self.pwd = pwd
        self.url = Test_Url(self.ip, self.usr, self.pwd)


    def dial(self, dst_ext, account='Account=1'):

        check_dial = False
        # 定义拨号url，使用ActionURL方式拨号
        self.url_dial = self.url.prefix + '/Phone_ActionURL&Command=1&Number=' + dst_ext + '&' + account
        # print(self.url_dial)
        try:
            r_dial = requests.get(self.url_dial, timeout=1)
            if r_dial.status_code == 200:
                time.sleep(1)
                if check_status('outgoing', self.ip):
                    check_dial = True
                    log.info(self.ip + ' dial ' + dst_ext + ' success.')
                else:
                    log.info(self.ip + ' dial failed.')
            else:
                log.info(self.ip + ' Return ' + r_dial.status_code + ', Dial Failed.')

        except requests.exceptions.ConnectionError:
            log.info(self.url_dial + ' Connection Error.')

        return check_dial


    def answer(self):

        check_answer = False
        self.url_answer = self.url.keyboard + 'F1'
        try:
            r_answer = requests.get(self.url_answer, timeout=1)
            if r_answer.status_code == 200:
                time.sleep(1)
                # 验状态失败不一定执行失败，再看截图
                if check_status('talking', self.ip):
                    check_answer = True
                    log.info(self.ip + ' answered the call.')
                else:
                    log.info(self.ip + ' answer maybe failed.')
            else:
                log.info(self.ip + ' Return ' + str(r_answer.status_code) + ', Answer Failed.')
        except requests.exceptions.ConnectionError:
            log.info(self.url_answer + ' Connection Error.')

        return check_answer


    def end_call(self, cmd):

        check_end = False
        self.url_end = self.url.keyboard + cmd.upper()
        try:
            r_end = requests.get(self.url_end, timeout=1)
            if r_end.status_code == 200:
                time.sleep(1)
                if check_status('idle', self.ip):
                    check_end = True
                    log.info(self.ip + ' The call ended.')
                else:
                    log.info(self.ip + ' end call failed.')
            else:
                log.info(self.ip + ' Return ' + str(r_end.status_code) + ', End call failed.')
        except requests.exceptions.ConnectionError:
            log.info(self.url_end + ' Connection Error.')

        return check_end


    def get_memory(self):

        check_get_memory = False
        pat_untag = r'(?<=\>)(.*)(?=\<)'
        self.url_memory = self.url.get_memory
        try:
            r_mem = requests.get(self.url_memory, timeout=1)
            if r_mem.status_code == 200:
                check_get_memory = True
                mem_info = re.findall(pat_untag, r_mem.text)
                log.info(mem_info)
            else:
                log.info('Get memory failed, return ' + r_mem.status_code)
        except requests.exceptions.ConnectionError:
            log.info(self.url_memory + ' Connection Error.')

        return check_get_memory


    def screen_shot(self):

        check_screen_shot = False
        self.url_screen_shot = self.url.screenshot
        try:
            r_screen_shot = requests.get(self.url_screen_shot, timeout=1)
            if r_screen_shot.status_code == 200:
                cur_time = time.strftime("%m%d_%H%M%S", time.localtime())
                with open(self.)
                check_screen_shot = True
                log.info('Capture Screenshot Success.')
            else:
                log.info('Capture Screenshot failed, return ' + r_screen_shot.status_code)
        except requests.exceptions.ConnectionError:
            log.info(self.cap_screen)

        return check_screen_shot


for i in range(num_dut):
    p_list.append(Phone(ip_list[i], ext_list[i]))
