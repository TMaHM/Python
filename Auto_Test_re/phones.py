import requests
import re
import os

from configs import *

class Phone():
    def __init__(self, ip, extension=None, usr='admin', pwd='admin'):
        self.ip = ip
        self.ext = extension
        self.usr = usr
        self.pwd = pwd
        self.url()

    def url(self):
        self.url_prefix = 'http://' + self.usr + ':' + self.pwd + '@' + self.ip

        self.url_screenshot = self.url_prefix + '/download_screen'
        self.url_keyboard = self.url_prefix + '/AutoTest&keyboard='
        self.url_check_status = self.url_prefix + '/AutoTest&autoverify=STATE='
        self.url_get_memory = self.url_prefix + '/AutoTest&autoverify=MEMORYFREE'
        self.url_setting = self.url_prefix + '/AutoTest&setting='

    def dial(self, dst_ext, account='Account=1'):

        self.url_dial = self.url_prefix + '/Phone_ActionURL&Command=1&Number=' + dst_ext + '&' + account
        # print(self.url_dial)
        try:
                r_dial = requests.get(self.url_dial, timeout=1)
                if r_dial.status_code == 200:
                    log.info(self.ip + ' dial ' + dst_ext + ' success.')

        except requests.exceptions.ConnectionError:
            log.info(self.url_dial + 'Connection Error.')





    def answer(self):
        print(self.url_keyboard + 'F1')

    def end_call(self, cmd):
        print(self.url_keyboard + cmd)

    def get_memory(self):
        print(self.url_get_memory)

    def screen_shot(self):
        print(self.url_screenshot)



for i in range(len(ip_list)):
    p_list.append(Phone(ip_list[i], ext_list[i]))