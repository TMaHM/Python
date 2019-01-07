import requests
import re
import os

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

        self.url_dial = self.url.prefix + '/Phone_ActionURL&Command=1&Number=' + dst_ext + '&' + account
        # print(self.url_dial)
        try:
                r_dial = requests.get(self.url_dial, timeout=1)
                if r_dial.status_code == 200:
                    check_status('outgoing', self.ip)
                    log.info(self.ip + ' dial ' + dst_ext + ' success.')

        except requests.exceptions.ConnectionError:
            log.info(self.url_dial + 'Connection Error.')





    def answer(self):
        print(self.url.keyboard + 'F1')

    def end_call(self, cmd):
        print(self.url.keyboard + cmd)

    def get_memory(self):
        print(self.url.get_memory)

    def screen_shot(self):
        print(self.url.screenshot)


for i in range(num_dut):
    p_list.append(Phone(ip_list[i], ext_list[i]))